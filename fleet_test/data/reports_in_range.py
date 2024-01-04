import json
from datetime import datetime as datetime, timedelta, timezone

# reports = {
#     "objects":[
#             {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-01 00:00:00",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-02 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-03 00:00:00",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-05 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-10 00:00:00",
#             "is_serviceable": False
#         },
#                 {
#             "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-14 00:00:00",
#             "is_serviceable": False
#         },
#         # start date Jan 16
#         {
#             "report_uuid": "f93f2f4f-8fff-4c5a-ad22-d9a330e4f8c9",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-18 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "c6215a43-3fec-42b9-824c-f9c397571532",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-05 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "57120477-5f25-4389-a0b1-f0e2b0d93c32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "f022c768-6ecd-45d1-919d-cb0d8c1e6b32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-10 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "ac4f16c7-d19e-4be2-8b2d-01be24f4311f",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-15 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-16 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-18 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-25 00:00:00",
#             "is_serviceable": False
#         },
#         # end date May 28
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-06-08 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-06-18 00:00:00",
#             "is_serviceable": True
#         },
#     ],
# }


# reports = {
#     "objects":[
#         {
#             "report_uuid": "91d8134b-163c-4cbd-b4ca-075804e97892",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2022-08-11 18:47:55",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-05 21:08:12",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-10 18:50:30",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "f93f2f4f-8fff-4c5a-ad22-d9a330e4f8c9",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-18 18:25:23",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "c6215a43-3fec-42b9-824c-f9c397571532",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 16:49:53",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "57120477-5f25-4389-a0b1-f0e2b0d93c32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 16:50:59",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "f022c768-6ecd-45d1-919d-cb0d8c1e6b32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 16:52:19",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "ac4f16c7-d19e-4be2-8b2d-01be24f4311f",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 21:20:32",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-16 17:39:55",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-16 17:40:41",
#             "is_serviceable": None
#         }
#     ],

# }


reports = [
        {   "report_uuid": "11/16 start-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-11-16 17:40:41",
            "is_serviceable": False
        },
        {    "report_uuid": "23/2 end-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-02-07 16:50:59",
            "is_serviceable": True
        },
        {    "report_uuid": "8/11 start-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2022-08-11 18:47:55",
            "is_serviceable": False
        },
        {    "report_uuid": "5/16 end-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-05-16 17:39:55",
            "is_serviceable": True
        },
        {    "report_uuid": "1/5 end-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-01-05 21:08:12",
            "is_serviceable": True
        },
        {    "report_uuid": "None",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-09-07 21:20:32",
            "is_serviceable": None
        },
        {    "report_uuid": "3/17 start-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-03-17 16:49:53",
            "is_serviceable": False
        },
        {    "report_uuid": "1/10 end-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-01-10 18:50:30",
            "is_serviceable": True
        },
        {    "report_uuid": "3/7 end-report",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-03-07 16:52:19",
            "is_serviceable": True
        },
        {    "report_uuid": "none",
            "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
            "vehicle_name": "A4",
            "created_at": "2023-01-18 18:25:23",
            "is_serviceable": None
        }
    ]



range_start = datetime.strptime("2023-01-16", '%Y-%m-%d')
range_end = datetime.strptime("2023-05-28", '%Y-%m-%d') 


def filter_reports_in_range(reports, range_start, range_end):
    sorted_reports = sorted(reports, key=lambda x: x["created_at"])

    reports_in_range = []  # List to store reports within the specified date range
    filtered_reports_for_calc = []  # List to store the final filtered reports

    for index, report in enumerate(sorted_reports):
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")
        
        # Check if the report is within the specified date range
        if range_start <= report_date <= range_end:
            reports_in_range.append(report)

            # Keep track of the index for the first report in the filtered range
            if len(reports_in_range) == 1:
                index_for_first_filtered_entry = index

    if len(reports_in_range) < 1:
        print("no reports in range")
        return

    last_report_in_range = reports_in_range[-1]

    if last_report_in_range["is_serviceable"] is False:
        print("dowtime ends after range")

        # If the last report in the range is not serviceable, add a dummy report
        last_report_for_calc = {
            "report_uuid": "downtime ends after range",
            "vehicle_uuid": last_report_in_range["vehicle_uuid"],
            "vehicle_name": last_report_in_range["vehicle_name"],
            "created_at": range_end.strftime("%Y-%m-%d %H:%M:%S"),
            "is_serviceable": True
        }

        reports_in_range.append(last_report_for_calc)
    else:
        filtered_reports_for_calc = reports_in_range

    # Check if there is a report before the date range
    if index_for_first_filtered_entry:
        report_before_date_range = sorted_reports[index_for_first_filtered_entry - 1]
        serviceable_before_range = report_before_date_range["is_serviceable"]

        if serviceable_before_range is True or serviceable_before_range is None:
            # downtime_starts_before_range = False
            print("dowtime starts in range")
            filtered_reports_for_calc = reports_in_range

        elif serviceable_before_range is False:
            print("dowtime starts before range")
            # downtime_starts_before_range = True
            first_report_for_calc = {
            "report_uuid": "downtime starts before range",
            "vehicle_uuid": report_before_date_range["vehicle_uuid"],
            "vehicle_name": report_before_date_range["vehicle_name"],
            # "vehicle_asset_number": report_before_date_range["vehicle_asset_number"],
            "created_at": range_start.strftime("%Y-%m-%d %H:%M:%S"),
            "is_serviceable": serviceable_before_range
        }

            filtered_reports_for_calc = [first_report_for_calc] + reports_in_range
    else:
        print("no inspections prior to date range")
        # downtime_starts_before_range = False

    return filtered_reports_for_calc


reports_for_calc = filter_reports_in_range(reports, range_start, range_end)

print("reports_for_calc =",reports_for_calc)


