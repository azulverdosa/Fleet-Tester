import datetime

from vammas166_downtime_reports import downtimeReports
# from leftblower_downtime_reports import downtimeReports

# date1 = '2022-06-08 18:56:12'
# date2 = '2023-11-21 11:45:29'

# start = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
# end = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
# total_hrs = end-start

# print(total_hrs)

all_downtimes = []

for report in downtimeReports:
    start_time = datetime.datetime.strptime(report['start']['datetime'], "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(report['end']['datetime'], "%Y-%m-%d %H:%M:%S")
    downtime = end_time - start_time
    
    print("Downtime:", downtime)

# Option 1:
downtime_total = datetime.timedelta()  # Initialize the total downtime as timedelta

for report in downtimeReports:
    downtime_str = report['downtime']
    days, time = downtime_str.split(', ')
    days = int(days.split()[0])  # Extract the number of days
    hours, minutes, seconds = map(int, time.split(':'))  # Extract hours, minutes, and seconds

    downtime = datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    downtime_total += downtime

print("Option 1 Total Downtime:", downtime_total)


# Option 2:
total_downtime = datetime.timedelta()  # Initialize the total downtime as timedelta

for report in downtimeReports:
    start_time = datetime.datetime.strptime(report['start']['datetime'], "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(report['end']['datetime'], "%Y-%m-%d %H:%M:%S")
    downtime = end_time - start_time
    
    total_downtime += downtime

print("Option 2 Total Downtime:", total_downtime)