import json
from datetime import datetime as datetime, timedelta, timezone

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
range_end = datetime.strptime("2023-02-03", '%Y-%m-%d') 



def filter_reports_in_range(reports, range_start, range_end):
    sorted_reports = sorted(reports, key=lambda x: x["created_at"])
    reports_in_range = []  
    filtered_reports_for_calc = []  
    previous_report_before_range_start = None
    was_serviceable_before_date_range = None
    last_report_in_range = None

    for report in sorted_reports:
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")
        
        if range_start <= report_date <= range_end:
            reports_in_range.append(report)

    for report in reversed(sorted_reports):
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")

        if report_date > range_start:
            continue

        if report_date < range_start:
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
                "created_at": range_end.strftime("%Y-%m-%d %H:%M:%S"),
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
                "created_at": range_start.strftime("%Y-%m-%d %H:%M:%S"),
                "is_serviceable": was_serviceable_before_date_range
            }

            filtered_reports_for_calc = [first_report_for_calc] + reports_in_range

    else:
        if was_serviceable_before_date_range is False:
            first_report_for_calc = {
                "report_uuid": "downtime starts before range",
                "vehicle_uuid": "No report available",
                "vehicle_name":"No report available",
                "created_at": range_start.strftime("%Y-%m-%d %H:%M:%S"),
                "is_serviceable": was_serviceable_before_date_range
            }

            last_report_for_calc = {
                "report_uuid": "downtime ends after range - downtime is entire date range",
                "vehicle_uuid": "No report available",
                "vehicle_name": "no report available",
                "created_at": range_end.strftime("%Y-%m-%d %H:%M:%S"),
                "is_serviceable": False
            }

            filtered_reports_for_calc = [first_report_for_calc, last_report_for_calc]

    return filtered_reports_for_calc

reports_for_calc = filter_reports_in_range(reports, range_start, range_end)

print("reports_for_calc =",reports_for_calc)