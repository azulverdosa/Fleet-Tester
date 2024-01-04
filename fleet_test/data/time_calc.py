import json
from datetime import datetime as datetime, timedelta, timezone

reports = {
    "objects":[
            {
            "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-01 00:00:00",
            "is_serviceable": None
        },
        {
            "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-02 00:00:00",
            "is_serviceable": False
        },
        {
            "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-03 00:00:00",
            "is_serviceable": None
        },
        {
            "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-05 00:00:00",
            "is_serviceable": False
        },
        {
            "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-10 00:00:00",
            "is_serviceable": False
        },
                {
            "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-14 00:00:00",
            "is_serviceable": False
        },
        # start date Jan 16
        {
            "report_uuid": "f93f2f4f-8fff-4c5a-ad22-d9a330e4f8c9",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-18 00:00:00",
            "is_serviceable": True
        },
        {
            "report_uuid": "c6215a43-3fec-42b9-824c-f9c397571532",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-03-05 00:00:00",
            "is_serviceable": True
        },
        {
            "report_uuid": "57120477-5f25-4389-a0b1-f0e2b0d93c32",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-03-07 00:00:00",
            "is_serviceable": True
        },
        {
            "report_uuid": "f022c768-6ecd-45d1-919d-cb0d8c1e6b32",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-03-10 00:00:00",
            "is_serviceable": False
        },
        {
            "report_uuid": "ac4f16c7-d19e-4be2-8b2d-01be24f4311f",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-03-15 00:00:00",
            "is_serviceable": False
        },
        {
            "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-05-16 00:00:00",
            "is_serviceable": True
        },
        {
            "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-05-18 00:00:00",
            "is_serviceable": True
        },
        {
            "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-05-25 00:00:00",
            "is_serviceable": False
        },
        # end date May 28
        {
            "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-06-08 00:00:00",
            "is_serviceable": True
        },
        {
            "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-06-18 00:00:00",
            "is_serviceable": True
        },
    ],
}


range_start = datetime.strptime("2023-01-16", '%Y-%m-%d')
range_end = datetime.strptime("2023-05-28", '%Y-%m-%d') 


def filter_reports_for_date_range(reports, range_start, range_end):
    reports_in_range = []
    filtered_reports = []

    print('1', filtered_reports)

    for index, report in enumerate(reports["objects"]):
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")

        if range_start <= report_date <= range_end:
            reports_in_range.append(report)

            if len(reports_in_range) == 1:
                first_filtered_entry_index = index # rename to indexForFirstFiltered or whatever

    last_report_in_range = reports_in_range[-1]

    print('2', reports_in_range)    
    
    if last_report_in_range["is_serviceable"] is False:
        last_report_for_calc = [
            {
            "report_uuid": "downtime ends after range",
            "vehicle_uuid": last_report_in_range["vehicle_uuid"],
            "vehicle_name": last_report_in_range["vehicle_name"],
            "created_at": range_end, #.strftime("%Y-%m-%d %H:%M:%S"),
            "is_serviceable": True
            }
        ]

        filtered_reports = reports_in_range.append(last_report_for_calc)

    else:
        filtered_reports = reports_in_range

    print('3', filtered_reports)

    if first_filtered_entry_index: # ugh names are hard
        report_before_date_range = reports["objects"][first_filtered_entry_index - 1]
        is_serviceable = report_before_date_range["is_serviceable"] # precision of variable name is insuficient, "what" is serviceable?
        # was serviceable before range

        if is_serviceable is True or is_serviceable is None:
            downtime_starts_before_range = False

        else:
            downtime_starts_before_range = True

    else: # this check should happen right after for loop
        print("no inspections prior to date range")

    if downtime_starts_before_range:
        first_report_for_calc = [
            {
            "report_uuid": "downtime starts before range",
            "vehicle_uuid": report_before_date_range["vehicle_uuid"],
            "vehicle_name": report_before_date_range["vehicle_name"],
            "created_at": range_end, #.strftime("%Y-%m-%d %H:%M:%S"),
            "is_serviceable": is_serviceable
            }
        ]

        filtered_reports = first_report_for_calc + reports_in_range

        # return filtered_reports

    else:
        filtered_reports = reports_in_range

    print('4', filtered_reports)

    return filtered_reports



filter_reports(reports, range_start, range_end)
