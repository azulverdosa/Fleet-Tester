from datetime import datetime

reports = {
    "objects":[
        {
            "report_uuid": "91d8134b-163c-4cbd-b4ca-075804e97892",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2022-08-11 18:47:55",
            "is_serviceable": True
        },
        {
            "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-05 21:08:12",
            "is_serviceable": True
        },
        {
            "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-10 18:50:30",
            "is_serviceable": True
        },
        {
            "report_uuid": "f93f2f4f-8fff-4c5a-ad22-d9a330e4f8c9",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-01-18 18:25:23",
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
            "created_at": "2023-03-07 16:50:59",
            "is_serviceable": True
        },
        {
            "report_uuid": "f022c768-6ecd-45d1-919d-cb0d8c1e6b32",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-03-07 16:52:19",
            "is_serviceable": True
        },
        {
            "report_uuid": "ac4f16c7-d19e-4be2-8b2d-01be24f4311f",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-03-07 21:20:32",
            "is_serviceable": None
        },
        {
            "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-05-16 17:39:55",
            "is_serviceable": True
        },
        {
            "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
            "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
            "vehicle_name": "A1",
            "created_at": "2023-05-16 17:40:41",
            "is_serviceable": None
        }
    ],

}

start_date = "2023-01-16"
end_date = "2023-05-28"

start_date = datetime.datetime.strptime("2023-01-16", "%Y-%m-%d")
# end_date = datetime.datetime.strptime("2023-05-28", "%Y-%m-%d")

entries_within_range = []

for report in reports["objects"]:
    created_at = datetime.datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")
    if start_date <= created_at <= end_date:
        entries_within_range.append(report)

print(entries_within_range)

# Specify the vehicle name and date range


# Calculate the total downtime




















# import datetime

# # from vammas166_downtime_reports import downtimeReports
# from leftblower_downtime_reports import downtimeReports

# date1 = '2022-06-08 18:56:12'
# date2 = '2023-11-21 11:45:29'

# start = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
# end = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
# total_hrs = end-start

# print(total_hrs)

# all_downtimes = []

# for report in downtimeReports:
#     start_time = datetime.datetime.strptime(report['start']['datetime'], "%Y-%m-%d %H:%M:%S")
#     end_time = datetime.datetime.strptime(report['end']['datetime'], "%Y-%m-%d %H:%M:%S")
#     downtime = end_time - start_time
    
#     print("Downtime:", downtime)

# # Option 1: maybe the right one
# downtime_total = datetime.timedelta()  # Initialize the total downtime as timedelta

# for report in downtimeReports:
#     downtime_str = report['downtime']
#     days, time = downtime_str.split(', ')
#     days = int(days.split()[0])  # Extract the number of days
#     hours, minutes, seconds = map(int, time.split(':'))  # Extract hours, minutes, and seconds

#     downtime = datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
#     downtime_total += downtime

# print("Option 1 Total Downtime:", downtime_total)


# # Option 2:
# total_downtime = datetime.timedelta()  # Initialize the total downtime as timedelta

# for report in downtimeReports:
#     start_time = datetime.datetime.strptime(report['start']['datetime'], "%Y-%m-%d %H:%M:%S")
#     end_time = datetime.datetime.strptime(report['end']['datetime'], "%Y-%m-%d %H:%M:%S")
#     downtime = end_time - start_time
    
#     total_downtime += downtime

# print("Option 2 Total Downtime:", total_downtime)