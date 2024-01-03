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


def find_date_range_reports(reports, range_start, range_end):
    filtered_inspections = []
    downtime_reports = []

    for index, entry in enumerate(reports["objects"]):
        created_at = datetime.strptime(entry["created_at"], "%Y-%m-%d %H:%M:%S")

        if range_start <= created_at <= range_end:
            filtered_inspections.append(entry)
            if len(filtered_inspections) == 1:
                first_filtered_entry_index = index

    if first_filtered_entry_index:
        first_before_date_range = reports["objects"][first_filtered_entry_index - 1]
        serviceable = first_before_date_range["is_serviceable"]

        print(serviceable)

        if serviceable is True or serviceable is None:
            downtime_starts_before_range = False
            
        # else:
        #     downtime_starts_before_range = True

        # if downtime_starts_before_range is True:
                    


        #     print(reports["objects"][first_filtered_entry_index - 1])   
        # print("previous serviceable:", first_before_date_range["is_serviceable"])


    # print("Filtered Inspections:")
    # for entry in filtered_inspections:
    #     print(entry)

    # print("Index of the first entry in filtered_inspections:", first_filtered_entry_index)


find_date_range_reports(reports, range_start, range_end)

# downtime_start = ''
# downtime_end = ''


# def filter_reports(reports, range_start = None, range_end = None):
#     filtered_reports = []
#     first_inspection_found = False

#     for report in reports["objects"]:
#         report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")

#         if range_start and report_date < range_start:
#             continue
#         elif not range_start:
#             first_inspection_found = True
#             first_
#             content = "Warning: Please enter a valid range start date"
#             return content

#         if range_end and report_date > range_end:
#             continue
#         elif not range_end:
#             content = "Warning: Please enter a valid range end date"
#             return content

#         filtered_report = {
#             'report_uuid': str(report["report_uuid"]),
#             'vehicle_uuid': str(report["vehicle_uuid"]),
#             'vehicle_name': report["vehicle_name"],
#             'created_at': report["created_at"],
#             'is_serviceable': report["is_serviceable"],
#         }
#         filtered_reports.append(filtered_report)
        
#     print(filtered_reports)

#     return filtered_reports


# def create_downtime_report(filtered_reports):
#     reports_for_downtime_calc = filtered_reports.sort(key=lambda x: x["created_at"])

#     downtime_reports = []

#     total_downtime = timedelta()

#     ignore_next_false = False

#     for entry in reports_for_downtime_calc:
#         if ignore_next_false:
#             if entry["is_serviceable"] is True:
#                 ignore_next_false = False
#             continue

#         if entry["is_serviceable"] is False:
#             downtime_start = entry["created_at"]
#             starting_report = entry["report_uuid"]
#             downtime_end = None

#             for sub_entry in reports_for_downtime_calc[reports_for_downtime_calc.index(entry):]:
#                 if sub_entry["is_serviceable"] is True or sub_entry["is_serviceable"] is None:
#                     downtime_end = sub_entry["created_at"]
#                     ending_report = sub_entry["report_uuid"]
#                     break

#             if downtime_end is None and downtime_start is not None:
#                 downtime_end = range_end
#                 ending_report = None

#             if downtime_end is not None and downtime_start is not None:
#                 try:
#                     calc_end = datetime.strptime(downtime_end, "%Y-%m-%d %H:%M:%S")
#                     calc_start = datetime.strptime(downtime_start, "%Y-%m-%d %H:%M:%S")
#                     total_hrs = calc_end - calc_start

#                     total_downtime += total_hrs

#                 except ValueError:
#                     content = "Error: Failed to convert date/time string"
#                     return content

#             downtime_reports.append({
#                 "start": {
#                     "starting_report": starting_report,
#                     "datetime": downtime_start,
#                     "downtime_starts_outside_range": None
#                 },
#                 "end": {
#                     "ending_report": ending_report if downtime_end else None,
#                     "datetime": downtime_end if downtime_end else range_end,
#                     "downtime_ends_outside_range": None

#                 },
#                 "downtime": str(round(total_hrs.total_seconds() / 3600, 2)),
#             })

#             ignore_next_false = True
    
#     print(downtime_reports)


def find_downtime_dates(reports, range_start, range_end):
    global downtime_start
    global downtime_end
    sorted_reports_descending = sorted(reports["objects"], key=lambda x: datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M:%S"), reverse=True)
    last_inspection_within_range = None

    for report in sorted_reports_descending:
        instance_of_report ={
            'report_uuid': report['report_uuid'],
            'vehicle_uuid': report['vehicle_uuid'],
            'vehicle_name': report['vehicle_name'],
            'created_at': report['created_at'],
            'is_serviceable': report['is_serviceable']
        }
        report_date = datetime.strptime(report['created_at'], '%Y-%m-%d %H:%M:%S')
        serviceable = report['is_serviceable']
        previous_report = None

        if report_date < range_start:
            if serviceable is True or serviceable is None:
                downtime_started_within_range = True
                first_report = instance_of_report

                print("Downtime started within date range: ", first_report['created_at'])
                print('first', serviceable)
                
                break

            else:
                downtime_started_outside_range = True
                first_report = {
                    'report_uuid': report['report_uuid'],
                    'vehicle_uuid': report['vehicle_uuid'],
                    'vehicle_name': report['vehicle_name'],
                    'created_at': range_start,
                    'is_serviceable': report['is_serviceable']
                }

                print('first', serviceable)
                print("Downtime started outside of date range:", first_report['created_at'])
                break

        # if report_date < range_start and (serviceable is True or serviceable is None):
        #     status = "within" if serviceable is True else "outside of"
        #     print(f"Downtime started {status} date range: {report_date} Service: {serviceable}")
        #     previous_report = report

        #     previous_report_uuid = report["report_uuid"]
        #     previous_report_date = previous_report['created_at']

        #     downtime_start = range_start
        #     break

        if range_start <= report_date <= range_end:
            last_inspection_within_range = report
            print(range_end)
            print("serviceable", last_inspection_within_range['is_serviceable'])

            if last_inspection_within_range['is_serviceable'] is False:
                last_report = {
                    'report_uuid': report['report_uuid'],
                    'vehicle_uuid': report['vehicle_uuid'],
                    'vehicle_name': report['vehicle_name'],
                    'created_at': range_end,
                    'is_serviceable': report['is_serviceable']
                }

                print('last_inspection_within_range:', last_report['is_serviceable'])
                print("false", last_report)
                break

            else:
                last_report = instance_of_report

                print("true or null", last_report)
                print("Downtime End:", last_report["created_at"])
                print("range end", range_end)
                break


# filter_reports(reports, range_start, range_end)
# find_downtime_dates(reports, range_start, range_end)