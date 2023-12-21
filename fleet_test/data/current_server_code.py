# ORIGINAL CODE:
target_vehicle_uuid = query_dict.get('vehicleUuid')
downtime_reports = []
total_downtime = datetime.timedelta() # Initialize total_downtime as timedelta

ignore_next_false = False

    for entry in reports_for_downtime_calc:

        # Step 3: Ignore consecutive "is_servicable == False" -
        # added a variable ignore_next_false to keep track of whether consecutive instances of ["is_serviceable"] == False 
        # should be ignored. If ignore_next_false is set to True, it skips the iteration until it finds the first occurrence 
        # of ["is_serviceable"] == True. Once it finds the first ["is_serviceable"] == True, it resets ignore_next_false 
        # to False, allowing the code to process subsequent instances normally.
        if ignore_next_false:
            if entry["is_serviceable"] == True:
                ignore_next_false = False
            continue

        if entry["is_serviceable"] == False:
            # Step 4: Record the start time
            start_time = entry["created_at"]
            starting_report = entry["report_uuid"]

            # Step 5: Search for the first occurrence of "is_serviceable": True
            end_time = None
            for sub_entry in reports_for_downtime_calc[reports_for_downtime_calc.index(entry):]:
                if sub_entry["is_serviceable"] == True:
                    end_time = sub_entry["created_at"]
                    ending_report = sub_entry["report_uuid"]
                    break

            if end_time is not None and start_time is not None:
                end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
                start = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                total_hrs = end - start

                days = total_hrs.days
                hours, remainder = divmod(total_hrs.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                downtime = f"{days} days, {hours:02d}:{minutes:02d}:{seconds:02d}"

                # Accumulate downtime duration to the total_downtime
                total_downtime += total_hrs

            # Step 6: Append the downtime report to the list
            downtime_reports.append({
                "start": {
                    "starting_report": starting_report,
                    "datetime": start_time
                },
                "end": {
                    "ending_report": ending_report if end_time else None,
                    "datetime": end_time if end_time else str(datetime.datetime.now())
                },
                "downtime": str(downtime),
            })

    # Step 8: Add desired values to time to the ret_obj
    ret_obj['dtreports'] = downtime_reports

    ret_obj['total time down'] = str(total_downtime)

    ret_obj['downtime_reports_count'] = len(downtime_reports)
    # downtime_reports.count()not work because downtime_reports does not have a .count() method.

    ret_obj['query_dict'] = query_dict.get('vehicleUuid')

    content, content_type = searchqueries.serialize_content(ret_obj)
    return HttpResponse(content, content_type)


# POE STEP BY STEP COMMENTS 
# Step 1: Retrieve Reports
target_vehicle_uuid = query_dict.get('vehicleUuid')
downtime_reports = []

def filter_reports(reports):
    filtered_reports = {
        'report_uuid': str(report.uuid),
        'vehicle_uuid': str(report.vehicle.uuid),
        'vehicle_name': report.vehicle.identifier,
        'created_at': report.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        'is_serviceable': report.is_serviceable
    }
    return filtered_reports

context._airport_id = request.airport.id

ret_obj = {}
reports_for_downtime_calc = []

# Check if return_objects is True and target_vehicle_uuid is provided
if return_objects and target_vehicle_uuid:
    # Retrieve all reports for the specified vehicle
    all_reports = models.Report.objects.filter(vehicle_id=target_vehicle_uuid)
    # Iterate over the reports based on the specified sorting and pagination parameters
    for report in all_reports.order_by(*sort)[skip:skip + count]:
        # Step 2: Filter the report details and add them to the list
        filtered_reports = filter_reports(all_reports)
        reports_for_downtime_calc.append(filtered_reports)

    # Add the filtered reports to the return object
    ret_obj['ONE_vehicle_reports_for_downtime_calc'] = reports_for_downtime_calc

# Check if return_objects is True and target_vehicle_uuid is not provided
elif return_objects and not target_vehicle_uuid:
    # Retrieve all reports based on the search criteria
    all_reports = models.Report.objects.filter(*search)
    # Iterate over the reports based on the specified sorting and pagination parameters
    for report in all_reports.order_by(*sort)[skip:skip + count]:
        # Step 2: Filter the report details and add them to the list
        filtered_reports = filter_reports(all_reports)
        reports_for_downtime_calc.append(filtered_reports)

    # Add the filtered reports to the return object
    ret_obj['ALL_vehicles_reports_for_downtime_calc'] = reports_for_downtime_calc

# Sort the reports based on the 'created_at' field
reports_for_downtime_calc.sort(key=lambda x: x["created_at"])

downtime_reports = []
total_downtime = datetime.timedelta()

# Iterate over the filtered reports to calculate downtime
for entry in reports_for_downtime_calc:
    if entry["is_serviceable"] == False:
        # Step 3: Record the start time
        start_time = entry["created_at"]
        starting_report = entry["report_uuid"]

        # Step 4: Search for the first occurrence of "is_serviceable": True
        end_time = None
        for sub_entry in reports_for_downtime_calc[reports_for_downtime_calc.index(entry):]:
            if sub_entry["is_serviceable"] == True:
                end_time = sub_entry["created_at"]
                ending_report = sub_entry["report_uuid"]
                break

        # Calculate the downtime duration if start and end times are available
        if end_time is not None and start_time is not None:
            end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            start = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            total_hrs = end - start

            days = total_hrs.days
            hours, remainder = divmod(total_hrs.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            downtime = f"{days} days, {hours:02d}:{minutes:02d}:{seconds:02d}"

            # Accumulate downtime duration to the total_downtime
            total_downtime += total_hrs

        # Step 5: Append the downtime report to the list
        downtime_reports.append({
            "start": {
                "starting_report": starting_report,
                "datetime": start_time
            },
            "end": {
                "ending_report": ending_report if end_time else None,
                "datetime": end_time if end_time else str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            },
            "downtime": str(downtime),
        })

# Add the downtime reports and related information to the return object
ret_obj['dtreports'] = downtime_reports
ret_obj['total time down'] = str(total_downtime)
ret_obj['all_reports_count'] = len(downtime_reports)
ret_obj['query_dict'] = query_dict.get('vehicleUuid')
