from datetime import datetime

reports = [
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
            "vehicle_name": "Vammas 166",
            "created_at": "2023-07-18 19:58:51",
            "is_serviceable": True
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
            "vehicle_name": "Vammas 166",
            "created_at": "2023-07-05 17:07:32",
            "is_serviceable": False
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "1dc9f8da-9818-446d-ba37-9cca161d22d0",
            "vehicle_name": "Left Blower 188",
            "created_at": "2023-11-11 16:56:16",
            "is_serviceable": True
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "1dc9f8da-9818-446d-ba37-9cca161d22d0",
            "vehicle_name": "Left Blower 188",
            "created_at": "2023-05-28 14:46:19",
            "is_serviceable": True
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
            "vehicle_name": "Vammas 166",
            "created_at": "2023-07-14 19:06:46",
            "is_serviceable": True
        },
        {
            "hours": 1,
            "kilometers": 12,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "70c56a2c-31ba-495b-a090-a8cbc60d1a24",
            "vehicle_name": "Delorean 1984",
            "created_at": "2023-01-11 15:37:04",
            "is_serviceable": True
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
            "vehicle_name": "Vammas 166",
            "created_at": "2023-06-29 19:38:29",
            "is_serviceable": None
        },
        {
            "hours": None,
            "kilometers": 121,
            "isUnsafe": True,
            "isRecurrent": True,
            "vehicle_uuid": "da0fe2b4-c676-4298-9f26-b69dc81a53e3",
            "vehicle_name": "liu test Vehicle",
            "created_at": "2023-01-12 20:53:51",
            "is_serviceable": True
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
            "vehicle_name": "Vammas 166",
            "created_at": "2023-07-18 20:05:01",
            "is_serviceable": True
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0ef1eb16-bc3e-49e3-85c8-b626199ec454",
            "vehicle_name": "A6",
            "created_at": "2023-04-10 19:52:38",
            "is_serviceable": None
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
            "vehicle_name": "Vammas 166",
            "created_at": "2023-07-13 20:37:53",
            "is_serviceable": None
        },
    ]


range_start = "2023-01-16 00:00:00" 
range_end = "2023-05-28 14:46:19"

def filter_reports_in_range(reports, range_start, range_end):
    sorted_reports = sorted(reports, key=lambda x: x["created_at"]) #TODO Don't think I need this

    reports_in_range = [] 
    filtered_reports_for_calc = []  

    # TODO what of the top 2 make more sense?
    if range_start is None or range_end is None:
        print("Invalid date range: Start or end date is missing.")
    elif not range_start or not range_end:
        print("Invalid date range: Start or end date is empty.")
    elif range_start > range_end:
        print("Invalid date range: Start date is after the end date.")


    for index, report in enumerate(sorted_reports):
        report_date = report["created_at"]

        if range_start <= report_date <= range_end:
            reports_in_range.append(report)

            if len(reports_in_range) == 1:
                index_for_first_filtered_entry = index

    if len(reports_in_range) < 1:
        print("no reports in range")
        return

    last_report_in_range = reports_in_range[-1]

    if last_report_in_range["is_serviceable"] is False:
        print("dowtime ends after range")

        last_report_for_calc = {
            "report_uuid": "downtime ends after range",
            "vehicle_uuid": last_report_in_range["vehicle_uuid"],
            # 'vehicle_asset_number':report.vehicle.asset_number,
            "vehicle_name": last_report_in_range["vehicle_name"],
            "created_at": range_end,
            "is_serviceable": True
        }

        reports_in_range.append(last_report_for_calc)
    else:
        filtered_reports_for_calc = reports_in_range

    if index_for_first_filtered_entry:
        report_before_date_range = sorted_reports[index_for_first_filtered_entry - 1]
        serviceable_before_range = report_before_date_range["is_serviceable"]

        if serviceable_before_range is True or serviceable_before_range is None:
            print("dowtime starts in range")
            filtered_reports_for_calc = reports_in_range

        elif serviceable_before_range is False:
            print("dowtime starts before range")
            first_report_for_calc = {
            "report_uuid": "downtime starts before range",
            "vehicle_uuid": report_before_date_range["vehicle_uuid"],
            "vehicle_name": report_before_date_range["vehicle_name"],
            # 'vehicle_asset_number':report.vehicle.asset_number, #TODO add in for main function
            "created_at": range_start,
            "is_serviceable": serviceable_before_range
        }

            filtered_reports_for_calc = [first_report_for_calc] + reports_in_range
    else:
        print("no inspections prior to date range")

    return filtered_reports_for_calc


reports_for_calc = filter_reports_in_range(reports, range_start, range_end)

print("reports_for_calc =",reports_for_calc)


def filter_reports(reports):
    filtered_reports = []

    for report in reports:
        filtered_report = {
            # 'report_uuid': "eport['report_uuid']", #TODO add in for main function
            'vehicle_uuid': report['vehicle_uuid'],
            'vehicle_name': report["vehicle_name"],
            # 'vehicle_asset_number':report.vehicle.asset_number, #TODO add in for main function
            'created_at': report["created_at"],
            'is_serviceable': report["is_serviceable"],
        }
        filtered_reports.append(filtered_report)

    return filtered_reports

print("filter_reports",filter_reports(reports_for_calc))