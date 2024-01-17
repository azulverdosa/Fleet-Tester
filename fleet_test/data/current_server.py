def filter_reports_in_range(reports, range_start, range_end): 
    sorted_reports = sorted(reports, key=lambda x: x["created_at"])

    reports_in_range = []  
    filtered_reports_for_calc = []  

    for index, report in enumerate(sorted_reports):
        report_date = report["created_at"]


        if range_start <= report_date <= range_end:
            reports_in_range.append(report)

            if len(reports_in_range) == 1:
                index_for_first_filtered_entry = index

    if len(reports_in_range) < 1:
        return

    last_report_in_range = reports_in_range[-1]

    if last_report_in_range["is_serviceable"] is False:

        # If the last report in the range is not serviceable, add a dummy report
        last_report_for_calc = {
            "report_uuid": "downtime ends after range",
            "vehicle_uuid": last_report_in_range["vehicle_uuid"],
            "vehicle_name": last_report_in_range["vehicle_name"],
            # "vehicle_asset_number": last_report_in_range["vehicle_asset_number"],
            "created_at": range_end,
            "is_serviceable": False
        }

        reports_in_range.append(last_report_for_calc)

    else:
        filtered_reports_for_calc = reports_in_range


    if index_for_first_filtered_entry:
        report_before_date_range = sorted_reports[index_for_first_filtered_entry - 1]
        serviceable_before_range = report_before_date_range["is_serviceable"]

        if serviceable_before_range is True or serviceable_before_range is None:
            filtered_reports_for_calc = reports_in_range

        elif serviceable_before_range is False:
            
            first_report_for_calc = {
            "report_uuid": "downtime starts before range",
            "vehicle_uuid": report_before_date_range["vehicle_uuid"],
            "vehicle_name": report_before_date_range["vehicle_name"],
            "vehicle_asset_number": report_before_date_range["vehicle_asset_number"],
            "created_at": range_start,
            "is_serviceable": serviceable_before_range
        }

            filtered_reports_for_calc = [first_report_for_calc] + reports_in_range
    # else:
    #     content = "No inspections prior to date range"
    #     return HttpResponseServerError(content)

    return filtered_reports_for_calc