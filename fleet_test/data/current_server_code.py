def filter_reports(reports, range_start = None, range_end = None):
    reports_in_range = []
    filtered_reports = []

    for report in reports:
        report_date = str(report.created_at.date())

        if range_start and report_date < range_start:
            continue
        elif not range_start:
            content = "Warning: Please enter a valid range start date"
            return content

        if range_end and report_date > range_end:
            continue
        elif not range_end:
            content = "Warning: Please enter a valid range end date"
            return content

        filtered_report = {
            'report_uuid': str(report.uuid),
            'vehicle_uuid': str(report.vehicle.uuid),
            'vehicle_name': report.vehicle.identifier,
            'vehicle_asset_number':report.vehicle.asset_number,
            'created_at': report.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'is_serviceable': report.is_serviceable,
        }
        filtered_reports.append(filtered_report)

    return filtered_reports


def _downtime_report_render_get(request, vehicle_uuid):
    if not is_authorized(request, None, [['report.r', 'report.w']]):
        return HttpResponseForbidden('not authorized')

    context = Context()
    context._airport_id = str(request.airport.id)

    vehicle = None
    try:
        vehicle_uuid = uuid.UUID(vehicle_uuid)
        vehicle = models.Vehicle.objects.select_related('subarea').get(
            uuid=vehicle_uuid, airport_id=request.airport.id)
    except models.Vehicle.DoesNotExist:
        return HttpResponseNotFound('vehicle not found')

    output_type = request.GET.get('outputtype', None)
    if output_type is None:
        return HttpResponseBadRequest('\'outputyype\' missing')

    range_start = request.GET.get('startdate')
    if range_start is None:
        return HttpResponseBadRequest('\'startdate\' missing')
    
    range_start += ' 00:00:00'

    range_end = request.GET.get('enddate')
    if range_end is None:
        return HttpResponseBadRequest('\'enddate\' missing')
    else:
        current_time_UTC = datetime.now(timezone.utc).strftime("%H:%M:%S")
        range_end += ' ' + current_time_UTC 

    reports_for_downtime_calc = []
    vehicle_name = ''
    vehicle_asset_number = ''

    if vehicle_uuid:
        vehicle = models.Vehicle.objects.get(uuid=vehicle_uuid)

        vehicle_name = vehicle.identifier
        vehicle_asset_number = vehicle.asset_number

        vehicle_reports = models.Report.objects.filter(vehicle_id=vehicle_uuid)
        
        for report in vehicle_reports:
            filtered_reports = filter_reports([report], range_start, range_end)
            if filtered_reports:
                reports_for_downtime_calc.extend(filtered_reports)

            else:
                content = "Warning: No reports for that vehicle UUID"
                # return HttpResponse('No reports for that vehicle UUID', status=204)

    else:
        content = "Warning: No vehicle UUID provided"
        # return HttpResponseBadRequest('No vehicle UUID provided')

    reports_for_downtime_calc.sort(key=lambda x: x["created_at"])

    downtime_reports = []

    total_downtime = timedelta()

    ignore_next_false = False

    for entry in reports_for_downtime_calc:
        if ignore_next_false:
            if entry["is_serviceable"] is True or entry["is_serviceable"] is None:
                ignore_next_false = False
            continue

        if entry["is_serviceable"] is False:
            downtime_start = entry["created_at"]
            starting_report = entry["report_uuid"]
            downtime_end = None

            for sub_entry in reports_for_downtime_calc[reports_for_downtime_calc.index(entry):]:
                if sub_entry["is_serviceable"] is True or sub_entry["is_serviceable"] is None:
                    downtime_end = sub_entry["created_at"]
                    ending_report = sub_entry["report_uuid"]
                    break

            if downtime_end is None and downtime_start is not None:
                downtime_end = range_end
                ending_report = None

            if downtime_end is not None and downtime_start is not None:
                try:
                    calc_end = datetime.strptime(downtime_end, "%Y-%m-%d %H:%M:%S")
                    calc_start = datetime.strptime(downtime_start, "%Y-%m-%d %H:%M:%S")
                    total_hrs = calc_end - calc_start

                    total_downtime += total_hrs

                except ValueError:
                    content = "Error: Failed to convert date/time string"
                    return content

            downtime_reports.append({
                "start": {
                    "starting_report": starting_report,
                    "datetime": downtime_start,
                    "downtime_starts_outside_range": None
                },
                "end": {
                    "ending_report": ending_report if downtime_end else None,
                    "datetime": downtime_end if downtime_end else range_end,

                },
                "downtime": str(round(total_hrs.total_seconds() / 3600, 2)),
            })

            ignore_next_false = True

    vehicle_downtime_report = []

    if downtime_reports:
        vehicle_downtime_report.append({
            'airport_id':context._airport_id,
            'vehicle_name': vehicle_name,
            'vehicle_asset_number': vehicle_asset_number,
            'downtime_reports': downtime_reports,
            'total_downtime': round(total_downtime.total_seconds() / 3600, 2)
        })
    else:
        content = "Warning: no reports available"
        # return HttpResponse('There is no downtime to report in that timeframe')

    content = None
    content_type = None
    if output_type == 'csv':
        content = reportrender.csv(vehicle_downtime_report)
        content_type = 'text/csv'
    elif output_type == 'xlsx':
        content = reportrender.xlsx(vehicle_downtime_report)
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    else:
        return HttpResponseBadRequest('\'outputtype\' not recognized')

    return HttpResponse(content, content_type)