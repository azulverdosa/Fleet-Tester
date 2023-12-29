from datetime import datetime as datetime, timezone

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
            "created_at": "2023-06-18 00:00:00",
            "is_serviceable": True
        },
    ],
}

# Define the range start and end dates
range_start = datetime.strptime("2023-01-16", '%Y-%m-%d')
range_end = datetime.strptime("2023-05-28", '%Y-%m-%d') 

downtime_start = ''
downtime_end = ''

def filter_reports(reports, range_start=None, range_end=None):
    filtered_reports = []

    for report in reports["objects"]:
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")

        if range_start and report_date < range_start:
            continue
        elif not range_start:
            content = "Warning: Please enter a valid range start date"
            return content

        if range_end and report_date > range_end:
            continue
        elif not range_end:
            content = "Warning: Please enter a valid range end date"
            return content

        filtered_report = {
            'report_uuid': str(report["report_uuid"]),
            'vehicle_uuid': str(report["vehicle_uuid"]),
            'vehicle_name': report["vehicle_name"],
            # 'vehicle_asset_number':report.vehicle.asset_number,
            'created_at': report["created_at"],
            'is_serviceable': report["is_serviceable"],
        }
        filtered_reports.append(filtered_report)
        
    # print(filtered_reports)

    return filtered_reports


def find_downtime_start_date(reports, range_start, range_end):
    global downtime_start
    sorted_reports_descend = sorted(reports["objects"], key=lambda x: datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M:%S"), reverse=True)

    for report in sorted_reports_descend:
        report_date = datetime.strptime(report['created_at'], '%Y-%m-%d %H:%M:%S')
        serviceable = report['is_serviceable']
        previous_report = None

        if report_date < range_start:
            if serviceable is True or serviceable is None:
                print("Downtime started within date range: ", report_date, 'Service:', serviceable)
                break

            elif serviceable is False:
                previous_report = report
                previous_report_uuid = report["report_uuid"]
                previous_report_date = previous_report['created_at']

                downtime_start = range_start
                break
        
        if report_date > range_end:

                

    # print('Downtime started before date range on', previous_report_date)
    # print('Downtime start date: ', downtime_start)
    # print('previous_report_uuid: ', previous_report_uuid)

print("Before:", downtime_start)
find_downtime_start_date(reports, range_start)
print("After:", downtime_start)



# filter_reports(reports, range_start, range_end)

# find_downtime_start_date(reports, range_start)

