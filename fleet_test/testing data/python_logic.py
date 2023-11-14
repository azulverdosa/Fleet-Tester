from vammas166 import reports
import datetime

data = {
    "reports": [
        {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 19:58:51",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 17:07:32",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-14 19:06:46",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-06-29 19:38:29",
    "is_serviceable": None
    
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 20:05:01",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-13 20:37:53",
    "is_serviceable": None
    
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-14 20:38:46",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-14 21:19:01",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-05-24 17:15:16",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 21:18:20",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-06-29 19:25:26",
    "is_serviceable": None
    
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 13:09:01",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-13 21:33:53",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 17:01:34",
    "is_serviceable": None
    
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 13:27:00",
    "is_serviceable": None
    
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 19:24:37",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 19:48:18",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-17 21:46:16",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 19:24:17",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-10 17:18:42",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 18:24:57",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 19:23:12",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 19:04:09",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 14:55:45",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 13:05:00",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 16:58:25",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 21:47:59",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 21:19:06",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-06-29 15:23:50",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-06-29 15:13:19",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 13:37:16",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-10 17:17:34",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 15:34:17",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-04 20:55:23",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 18:27:39",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 19:44:24",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 15:14:02",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-17 21:50:55",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-18 18:32:33",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 16:20:25",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 18:25:22",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-11 13:23:13",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 13:06:52",
    "is_serviceable": True
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-19 20:27:15",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-06 18:54:34",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 19:03:00",
    "is_serviceable": None
      
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-13 21:36:15",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-06 19:27:17",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-05 16:59:16",
    "is_serviceable": False
    },
    {
    "vehicle_uuid": "0591a6fe-24f4-4392-8525-03f48a16fa90",
    "vehicle_name": "Vammas 166",
    "created_at (strftime)": "2023-07-10 17:18:13",
    "is_serviceable": False
    }
    ]
}

# Sort the reports chronologically based on the "created_at" timestamp. This step ensures that the reports are in ascending order based on time.

# Initialize variables to track the start and end timestamps for the "is_serviceable": false duration, as well as the total duration.

# Iterate through the sorted reports and perform the following steps for each report:

# Check if the "is_serviceable" value is false.
# If it is false, set the start timestamp if it has not been set already.
# If it is true and the start timestamp has been set, calculate the duration by subtracting the start timestamp from the current report's timestamp. Add this duration to the total duration.
# Reset the start timestamp to None.
# After iterating through all the reports, if the start timestamp is not None (indicating that the final report had "is_serviceable": false), calculate the duration from the start timestamp to the end of the time period (or the current time). Add this duration to the total duration.

# The total duration represents the duration for which the vehicle had "is_serviceable": false.

reports = data["reports"]
reports.sort(key=lambda x: x["created_at (strftime)"])

start_timestamp = None
total_duration = datetime.timedelta()

for report in reports:
    if not report["is_serviceable"]:
        if start_timestamp is None:
            start_timestamp = datetime.datetime.strptime(report["created_at (strftime)"], "%Y-%m-%d %H:%M:%S")
    elif start_timestamp is not None:
        current_timestamp = datetime.datetime.strptime(report["created_at (strftime)"], "%Y-%m-%d %H:%M:%S")
        duration = current_timestamp - start_timestamp
        total_duration += duration
        start_timestamp = None

# Check if the last report had "is_serviceable": false
if start_timestamp is not None:
    current_timestamp = datetime.datetime.now()
    duration = current_timestamp - start_timestamp
    total_duration += duration

print("Total duration with is_serviceable=False:", total_duration)


# TODO return should be:
# Total duration with is_serviceable=False: 170 days, 0:35:03.633941
# 
# This indicates that the vehicle had an "is_serviceable": false duration of 9 days, 1 hour, 59 minutes, and 14 seconds.

# --------------Javascript translated logic below by Poe ----------------------------------------------------------------------

# from report_data import data
# from datetime import datetime

# another_uuid = '2ffd6494-68ae-4b4b-8a54-d2b36181b44f'
# other_uuid = '0cc18e59-ee6a-4b0b-974a-2998686af408'
# bmw1_uuid = 'e844b8b3-f627-462b-9a1d-514a7b3f0831'
# multihog_uuid = '3ddf5d06-1323-4924-a038-203344e7d4c9'

# def get_milliseconds(date_str=None):
#     date_str = date_str or datetime.now().isoformat()
#     return int(datetime.fromisoformat(date_str).timestamp() * 1000)

# # this filter is not the one to use in real life
# # throwaway code: mocks missing database
# filtered = list(filter(lambda x: x['vehicleUuid'] == bmw1_uuid, reversed(data["objects"])))
# # end of throwaway

# results = {
#     'start': None,
#     'totalHours': 0
# }

# for index, report in enumerate(filtered):
#     is_last_report_in_range = index == len(filtered) - 1

#     if results['start'] is not None and report['isRTOInspectionRequired']:
#         print('fixxd!')
#         print('ended :>>', report['createdAt'])

#         downtime_milliseconds = get_milliseconds(report['createdAt']) - get_milliseconds(results['start'])
#         downtime_hours = round(downtime_milliseconds / 1000 / 60 / 60, 2)

#         print('previousDowntimeHours :>>', results['totalHours'])
#         print('downtimeHours :>>', downtime_hours)

#         results['totalHours'] += downtime_hours
#         results['start'] = None

#     elif report['isUnsafe']:
#         if results['start'] is not None:
#             print('still unsafe')
#         else:
#             print('it broke!')
#             print('start :>>', report['createdAt'])
#             results['start'] = report['createdAt']

#     print('usable')
#     if report['isRTOInspectionRequired']:
#         print('rto required')

# print('Total Hours :>>', results['totalHours'])