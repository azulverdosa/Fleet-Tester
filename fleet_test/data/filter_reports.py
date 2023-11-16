import datetime

from all_reports_all_data import all_reports
from a1 import reports as a1_reports

ret_obj = {}

target_vehicle_uuid = "1dc9f8da-9818-446d-ba37-9cca161d22d0"

def filter_reports_by_vehicle_uuid(all_reports, target_vehicle_uuid):
    filtered_reports = {
        "objects": []
    }

    for report in all_reports["objects"]:
        if report["vehicle_uuid"] == target_vehicle_uuid:
            filtered_reports["objects"].append(report)
    
    return filtered_reports

filtered_reports = filter_reports_by_vehicle_uuid(all_reports, target_vehicle_uuid)

# Print the filtered reports
# for report in filtered_reports["objects"]:
#     print(report)

def sort_reports_by_created_at(reports):
    sorted_reports = sorted(reports["objects"], key=lambda x: datetime.datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M:%S"))
    return sorted_reports

target_vehicle_uuid = "0591a6fe-24f4-4392-8525-03f48a16fa90"
filtered_reports = filter_reports_by_vehicle_uuid(all_reports, target_vehicle_uuid)
sorted_reports = sort_reports_by_created_at(filtered_reports)

# Print the sorted reports
for report in sorted_reports:
    print(report)