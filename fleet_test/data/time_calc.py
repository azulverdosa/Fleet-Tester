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
            "created_at": "2023-01-16 00:00:00",
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
range_start_date = datetime.strptime("2023-01-16", '%Y-%m-%d')
range_end_date = datetime.strptime("2023-05-28", '%Y-%m-%d') 

# Define a function to remove reports that are not serviceable within the specified range
def remove_none_serviceable_reports(reports):

    # Filter the reports to include only those with a non-null 'is_serviceable' value
    filtered_reports = [report for report in reports['objects'] if report.get('is_serviceable') is not None]

    # Sort the filtered reports in reverse order based on the 'created_at' date
    filtered_reports.sort(key=lambda x: datetime.strptime(x['created_at'], '%Y-%m-%d %H:%M:%S'), reverse=True)

    # Iterate over the filtered reports
    for report in filtered_reports:
        # Get the report's 'created_at' date and 'is_serviceable' value
        report_date = datetime.strptime(report['created_at'], '%Y-%m-%d %H:%M:%S')
        service = report['is_serviceable']
        previous_report = None

        # Check if the report's date is before the range start date
        if report_date < range_start_date:
            # Print the report's date and service value
            print('Report Date:', report_date, 'Service:', service)

            # Check if the service is True
            if service is True:
                # If so, return and print a message indicating there was no downtime before the range start date
                return print("NO downtime start before range start date")

            # Check if the service is False
            elif service is False:
                # If so, assign the current report to the previous_report variable
                previous_report = report
                start_date = range_start_date
                # Print the previous report's 'created_at' date
                print('Break:', previous_report['created_at'])
                # and assign the range start date to start_date
                print(start_date)
                # Print a message indicating downtime started before the range start date
                print('Downtime started before range start date')
                # Exit the loop
                break

# Call the function with the 'reports' data
remove_none_serviceable_reports(reports)
