    
from datetime import timedelta
import datetime


reports = [
        {
            "report_uuid": "91d8134b-163c-4cbd-b4ca-075804e97892",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2022-08-11 18:47:55",
            "is_serviceable": False
        },
        {
            "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-05 21:08:12",
            "is_serviceable": False
        },
        {
            "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-02-10 18:50:30",
            "is_serviceable": True
        },
        {
            "report_uuid": "f93f2f4f-8fff-4c5a-ad22-d9a330e4f8c9",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-02-28 18:25:23",
            "is_serviceable": None
        },
        {
            "report_uuid": "c6215a43-3fec-42b9-824c-f9c397571532",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-03-07 16:49:53",
            "is_serviceable": True
        },
        {
            "report_uuid": "57120477-5f25-4389-a0b1-f0e2b0d93c32",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-04-15 16:50:59",
            "is_serviceable": True
        },
        {
            "report_uuid": "f022c768-6ecd-45d1-919d-cb0d8c1e6b32",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-05-25 16:52:19",
            "is_serviceable": True
        },
        {
            "report_uuid": "ac4f16c7-d19e-4be2-8b2d-01be24f4311f",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-06-16 21:20:32",
            "is_serviceable": False
        },
        {
            "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-07-16 17:39:55",
            "is_serviceable": True
        },
        {
            "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-08-26 17:40:41",
            "is_serviceable": None
        }]
    

range_start = datetime.strptime("2023-01-28", '%Y-%m-%d')
range_end = datetime.strptime("2023-03-03", '%Y-%m-%d') 

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

    reports_for_date_range_search = []
    vehicle_name = ''
    vehicle_asset_number = ''

    if vehicle_uuid:
        vehicle = models.Vehicle.objects.get(uuid=vehicle_uuid)

        vehicle_name = vehicle.identifier
        vehicle_asset_number = vehicle.asset_number

        vehicle_reports = models.Report.objects.filter(vehicle_id=vehicle_uuid) #TODO investigate created_at__lt=range_start
        
        for report in vehicle_reports:
            filtered_reports = filter_report_data([report])

            if filtered_reports:
                reports_for_date_range_search.extend(filtered_reports)

            else:
                content = "Warning: No reports for that vehicle UUID"
                return HttpResponseServerError(content)

        reports_for_downtime_calc = filter_reports_in_range(reports_for_date_range_search, range_start, range_end, vehicle_uuid, vehicle_name, vehicle_asset_number)

        if reports_for_downtime_calc:
            content = "setup = ", reports_for_downtime_calc[3], "prev_report = ", reports_for_downtime_calc[0], ", reports_in_range =", reports_for_downtime_calc[1], ", filtered_reports_for_calc =", reports_for_downtime_calc[2]

        else:
            content = "No reports in range"
            return HttpResponseServerError(content)
        

        if not reports_for_downtime_calc:
            content = "Warning: No reports in range"
            return HttpResponseServerError(content)

    else:
        content = "Warning: No vehicle UUID provided"
        return HttpResponseServerError(content)

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
            downtime_start = datetime.strptime(entry["created_at"], "%Y-%m-%d %H:%M:%S")
            downtime_start_str = downtime_start.strftime("%Y-%m-%d %H:%M:%S")
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
                    calc_start = datetime.strptime(downtime_start_str, "%Y-%m-%d %H:%M:%S")
                    total_hrs = calc_end - calc_start

                    total_downtime += total_hrs

                except ValueError:
                    content = "Error: Failed to convert date/time string"
                    return HttpResponseServerError(content)

            downtime_reports.append({
                "starting_report": starting_report,
                "start_datetime": downtime_start,
                "ending_report": ending_report,
                "end_datetime": downtime_end if downtime_end else range_end,
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
        return HttpResponseServerError(content)

        # vehicle_downtime_report.append({
        #     'airport_id':context._airport_id,
        #     'vehicle_name': vehicle_name,
        #     'vehicle_asset_number': vehicle_asset_number,
        #     'downtime_reports': "No downtime to report",
        #     'total_downtime': round(total_downtime.total_seconds() / 3600, 2)
        # })
