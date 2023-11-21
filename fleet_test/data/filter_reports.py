from datetime import datetime, timedelta
import sys

from all_reports_all_data import all_reports
from a1 import reports as a1_reports
from all_dtreport_data import all_dtreports
from left_blower import reports as left_blower_reports

# ------------------ filter by vehicle 
desired_vehicle_uuid = "1dc9f8da-9818-446d-ba37-9cca161d22d0"

reports_by_vehicle = [
    report
    for report in left_blower_reports["objects"]
    if report["vehicle_uuid"] == desired_vehicle_uuid
]

# for report in reports_by_vehicle:
#     print(report)

# ------------------ sort chronologically
date_sorted_reports = sorted(reports_by_vehicle, key=lambda x: datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M:%S"))

# for report in date_sorted_reports:
#     print(report)

print(len(date_sorted_reports))

# ------------------ filter reports by values for downtime report

filtered_reports = [
    {
        "created_at": report["created_at"],
        "vehicle_uuid": report["vehicle_uuid"],
        "is_serviceable": report["is_serviceable"]
    }
    for report in date_sorted_reports
]

for report in filtered_reports:
    print(report)

