from datetime import datetime as datetime

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
            "created_at": "2023-01-13 00:00:00",
            "is_serviceable": None
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
            "created_at": "2023-03-07 00:00:00",
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
        {
            "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-06-18 00:00:00",
            "is_serviceable": True
        },
    ],
}

range_start_date = "2023-01-16"
range_end_date = '2023-05-28'

def remove_none_serviceable_reports(reports):
    start_date = datetime.strptime(range_start_date, '%Y-%m-%d') 
    print('111 - start', start_date)

    # filtered_reports = []

    # for report in reports['objects']:
    #     if report.get('is_serviceable') is not None:
    #         print(report['created_at'])

    #         filtered_reports.append(report)

    # more concise:
    filtered_reports = [report for report in reports['objects'] if report.get('is_serviceable') is not None]

    # for report in filtered_reports:
    #     print(report['created_at'])


    for report in filtered_reports:
        report_date = datetime.strptime(report['created_at'], '%Y-%m-%d %H:%M:%S')
        service = report['is_serviceable']
        previous_report = None

        if report_date < start_date:
            print('134 - ', report_date, service)

            if report.get('is_serviceable') is True:
                return print("No downtime before start date")
            
            elif report.get('is_serviceable') is False:
                previous_report = report
                print('140 - ', previous_report)

    #         elif report.get('is_serviceable') is False:
    #             previous_report = report
    #         else:
    #             break
    
    # # Iterate backwards in the data until we find a report with is_serviceable as True
    # if previous_report is not None:
    #     for report in reversed(reports['objects']):
    #         if report == previous_report:
    #             break
    #         if report.get('is_serviceable') is True:
    #             previous_report = report
    #             break
    
        if previous_report is not None:
            return print("143 - Downtime found before start date")
        else:
            return print("145 - No relevant reports before start date")
    
            

# def find_entries_before_start(filtered_reports):

remove_none_serviceable_reports(reports)



# def find_downtime_before_start_date(reports, start_date):
#     start_date = datetime.strptime(start_date, '%Y-%m-%d')
#     previous_report = None

#     for report in reports['objects']:
#         report_date = datetime.strptime(report['created_at'], '%Y-%m-%d %H:%M:%S')
#         if report_date < start_date:
#             if report.get('is_serviceable') is True:
#                 return "No downtime before start date"
#             elif report.get('is_serviceable') is False:
#                 previous_report = report
    
    # if previous_report is not None:
    #     return "Downtime found before start date"
    # else:
    #     return "No relevant reports before start date"

# start_date = "2023-01-18"
# result = find_downtime_before_start_date(reports, start_date)
# print(result)
