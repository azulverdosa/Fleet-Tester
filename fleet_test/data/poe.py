from datetime import datetime

def filter_reports(reports: dict, range_start: datetime, range_end: datetime) -> list:
    reports_in_range = []
    filtered_reports = []

    for index, report in enumerate(reports["objects"]):
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")

        if range_start <= report_date <= range_end:
            reports_in_range.append(report)
            last_report_in_range = reports_in_range[-1]

            if len(reports_in_range) == 1:
                first_filtered_entry_index = index

    if last_report_in_range["is_serviceable"] is False:
        last_report_for_calc = [
            {
                "report_uuid": "downtime ends after range",
                "vehicle_uuid": last_report_in_range["vehicle_uuid"],
                "vehicle_name": last_report_in_range["vehicle_name"],
                "created_at": range_end,
                "is_serviceable": True
            }
        ]
        reports_in_range.append(last_report_for_calc)
    else:
        filtered_reports = reports_in_range

    if first_filtered_entry_index:
        report_before_date_range = reports["objects"][first_filtered_entry_index - 1]
        is_serviceable = report_before_date_range["is_serviceable"]

        if is_serviceable is not False:
            downtime_starts_before_range = False
        else:
            downtime_starts_before_range = True
    else:
        print("no inspections prior to date range")
        downtime_starts_before_range = False

    if downtime_starts_before_range:
        first_report_for_calc = [
            {
                "report_uuid": "downtime starts before range",
                "vehicle_uuid": report_before_date_range["vehicle_uuid"],
                "vehicle_name": report_before_date_range["vehicle_name"],
                "created_at": range_start,
                "is_serviceable": is_serviceable
            }
        ]

        filtered_reports = first_report_for_calc + reports_in_range

    return filtered_reports


# Example usage
range_start = datetime.strptime("2023-01-16", '%Y-%m-%d')
range_end = datetime.strptime("2023-05-28", '%Y-%m-%d')

reports = {
    "objects": [
        {
            "created_at": "2023-01-15 23:59:59",
            "is_serviceable": False,
            "vehicle_uuid": "123",
            "vehicle_name": "Vehicle 1"
        },
        {
            "created_at": "2023-01-16 00:00:01",
            "is_serviceable": True,
            "vehicle_uuid": "456",
            "vehicle_name": "Vehicle 2"
        },
        # Add morereports here...
    ]
}

filtered_reports = filter_reports(reports, range_start, range_end)
print(filtered_reports)