import datetime

from all_reports_all_data import all_reports

ret_obj = {}

all_filtered_reports = [
    {
        "created_at": report["created_at"],
        "vehicle_uuid": report["vehicle_uuid"],
        "is_serviceable": report["is_serviceable"]
    }
    for report in all_reports["objects"]
]

all_filtered_reports_sorted_ASC = sorted(all_filtered_reports, key=lambda x: x["created_at"])

print(all_filtered_reports_sorted_ASC )

desired_vehicle_uuid = "1dc9f8da-9818-446d-ba37-9cca161d22d0"

filtered_reports_for_specific_vehicle = [
    report
    for report in all_filtered_reports_sorted_ASC
    if report["vehicle_uuid"] == desired_vehicle_uuid
]

# print(filtered_reports_for_specific_vehicle)

downtime_periods = []
start_time = None

for report in filtered_reports_for_specific_vehicle:
    if report["is_serviceable"] is False:
        if start_time is None:
            start_time = report["created_at"]
    else:
        if start_time is not None:
            end_time = report["created_at"]
            downtime_periods.append({"start_time": start_time, "end_time": end_time})
            start_time = None

# Check if the last report indicates a downtime still ongoing
if start_time is not None:
    end_time = "Current Time"  # Replace "Current Time" with the current time or any placeholder
    downtime_periods.append({"start_time": start_time, "end_time": end_time})

print(downtime_periods)

total_downtime_hours = 0

for period in downtime_periods:
    start_time = datetime.datetime.strptime(period["start_time"], "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(period["end_time"], "%Y-%m-%d %H:%M:%S")
    duration = end_time - start_time
    downtime_hours = duration.total_seconds() / 3600
    total_downtime_hours += downtime_hours

print("Total Downtime Hours:", total_downtime_hours)

total_downtime_days = total_downtime_hours / 24

print("Total Downtime Days:", total_downtime_days)

# total_downtime_days, remainder = divmod(total_downtime_hours, 24)
# total_downtime_hours, remainder = divmod(remainder * 60, 60)
# total_downtime_minutes, total_downtime_seconds = divmod(remainder * 60, 60)

# formatted_duration = f"{int(total_downtime_days)} days {int(total_downtime_hours)} hours, {int(total_downtime_minutes)} minutes, {int(total_downtime_seconds)} seconds"

# print("Total Downtime Duration:", formatted_duration)

