from report_data import data

filtered_data = [vehicle for vehicle in data["objects"] if vehicle["isServiceable"]]

for vehicle in filtered_data:
    print(vehicle["createdAt"])
    print(vehicle["vehicleUuid"])
    print(vehicle["isServiceable"])
    print()