import json
from datetime import datetime as datetime, timedelta, timezone

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
            "created_at": "2019-11-11 16:56:16",
            "is_serviceable": True
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "1dc9f8da-9818-446d-ba37-9cca161d22d0",
            "vehicle_name": "Left Blower 188",
            "created_at": "2019-05-28 14:46:19",
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
        {
            "hours": None,
            "kilometers": 11,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0ef1eb16-bc3e-49e3-85c8-b626199ec454",
            "vehicle_name": "A6",
            "created_at": "2023-04-10 21:36:54",
            "is_serviceable": None
        },
        {
            "hours": None,
            "kilometers": None,
            "isUnsafe": False,
            "isRecurrent": False,
            "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
            "vehicle_name": "Vammas 166",
            "created_at": "2023-07-14 20:38:46",
            "is_serviceable": True
        }]
    

range_start = "2023-01-28"
range_end = "2023-12-03"


def filter_reports_in_range(reports, range_start, range_end):
    sorted_reports = sorted(reports, key=lambda x: x["created_at"])
    reports_in_range = []  
    filtered_reports_for_calc = []  
    previous_report_before_range_start = None
    was_serviceable_before_date_range = None
    last_report_in_range = None
    range_start_converted = datetime.strptime(range_start, '%Y-%m-%d')
    range_end_converted = datetime.strptime(range_end, '%Y-%m-%d')
    

    for report in sorted_reports:
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")
        
        if range_start_converted <= report_date <= range_end_converted:
            reports_in_range.append(report)

    for report in reversed(sorted_reports):
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")

        if report_date > range_start_converted:
            continue

        if report_date < range_start_converted:
            previous_report_before_range_start = report
            was_serviceable_before_date_range = previous_report_before_range_start["is_serviceable"]
            break

    if reports_in_range:
        last_report_in_range = reports_in_range[-1]

        if last_report_in_range["is_serviceable"] is False:
            last_report_for_calc = {
                "report_uuid": "downtime ends after range",
                "vehicle_uuid": last_report_in_range["vehicle_uuid"],
                "vehicle_name": last_report_in_range["vehicle_name"],
                "created_at": range_end_converted,
                "is_serviceable": True
            }

            reports_in_range.append(last_report_for_calc)
            filtered_reports_for_calc = reports_in_range

        else:
            filtered_reports_for_calc = reports_in_range

        if was_serviceable_before_date_range is False:
            first_report_for_calc = {
                "report_uuid": "downtime starts before range",
                "vehicle_uuid": previous_report_before_range_start["vehicle_uuid"],
                "vehicle_name": previous_report_before_range_start["vehicle_name"],
                "created_at": range_start_converted,
                "is_serviceable": was_serviceable_before_date_range
            }

            filtered_reports_for_calc = [first_report_for_calc] + reports_in_range

    else:
        if was_serviceable_before_date_range is False:
            first_report_for_calc = {
                "report_uuid": "downtime starts before range",
                "vehicle_uuid": "No report available",
                "vehicle_name":"No report available",
                "created_at": range_start_converted,
                "is_serviceable": was_serviceable_before_date_range
            }

            last_report_for_calc = {
                "report_uuid": "downtime ends after range - downtime is entire date range",
                "vehicle_uuid": "No report available",
                "vehicle_name": "no report available",
                "created_at": range_start_converted,
                "is_serviceable": False
            }

            filtered_reports_for_calc = [first_report_for_calc, last_report_for_calc]

    return filtered_reports_for_calc

reports_for_calc = filter_reports_in_range(reports, range_start, range_end)

print("reports_for_calc =",reports_for_calc)


