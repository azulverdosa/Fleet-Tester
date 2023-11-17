from datetime import datetime, timedelta

from all_reports_all_data import all_reports
from a1 import reports as a1_reports
from all_dtreport_data import all_dtreports

# ------------------ filter by vehicle 
desired_vehicle_uuid = "0591a6fe-24f4-4392-8525-03f48a16fa90"

reports_by_vehicle = [
    report
    for report in all_dtreports["objects"]
    if report["vehicle_uuid"] == desired_vehicle_uuid
]

# for report in reports_by_vehicle:
#     print(report)
# print(reports_by_vehicle)

# ------------------ sort chronologically
date_sorted_reports = sorted(reports_by_vehicle, key=lambda x: datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M:%S"))

# for report in date_sorted_reports:
#     print(report)

# print(len(date_sorted_reports))
# # print(date_sorted_reports)

# ------------------ filter reports by values for downtime report

filtered_reports = [
    {
        "created_at": report["created_at"],
        "vehicle_uuid": report["vehicle_uuid"],
        "is_serviceable": report["is_serviceable"]
    }
    for report in date_sorted_reports
]

# # print(filtered_reports)

# ------------------ calculate downtime reports
downtime_reports = []

# Iterate over the filtered_reports
for i in range(len(date_sorted_reports)-1):
    current_report = date_sorted_reports[i]
    next_report = date_sorted_reports[i+1]

    # Check if current_report is_serviceable is False and next_report is_serviceable is True
    if not current_report['is_serviceable'] and next_report['is_serviceable'] is True:
        start_time = datetime.strptime(current_report['created_at'], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(next_report['created_at'], "%Y-%m-%d %H:%M:%S")
        total_hours = (end_time - start_time).total_seconds() / 3600

        downtime_report = {
            'start_time': start_time,
            'end_time': end_time,
            'total_hours': total_hours
        }

        downtime_reports.append(downtime_report)

# Print the downtime reports
print(len(downtime_reports)) 

for report in downtime_reports:
    print(report)

# ------------------ sum total_hours from downtime_reports
# Calculate the total downtime in seconds
total_downtime_seconds = sum(report['total_hours'] * 3600 for report in downtime_reports)

# Convert total_downtime_seconds to a timedelta object
total_downtime = timedelta(seconds=total_downtime_seconds)

print(total_downtime)
