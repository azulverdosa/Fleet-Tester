import datetime

# from a1 import reports
# from a2 import reports
# from a4 import reports
from vammas166 import reports
# from left_blower import reports

# Step 1: Sort the data by date (created_at) in ascending order
sorted_reports = sorted(reports["objects"], key=lambda x: datetime.datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M:%S"))

# Step 2: Iterate over the sorted data and search for entries with "is_serviceable": False
downtime_reports = []
total_downtime = datetime.timedelta() # Initialize total_downtime as timedelta

ignore_next_false = False

for entry in reports["objects"]:

    #  Step 3: Ignore consecutive "is_servicable == False" -
    # added a variable ignore_next_false to keep track of whether consecutive instances of ["is_serviceable"] == False 
    # should be ignored. If ignore_next_false is set to True, it skips the iteration until it finds the first occurrence 
    # of ["is_serviceable"] == True. Once it finds the first ["is_serviceable"] == True, it resets ignore_next_false 
    # to False, allowing the code to process subsequent instances normally.
    if ignore_next_false:
        if entry["is_serviceable"] == True:
            ignore_next_false = False
        continue

    if entry["is_serviceable"] == False:
        # Step 4: Record the start time
        start_time = entry["created_at"]
        starting_report = entry["report_uuid"]

        # Step 5: Search for the first occurrence of "is_serviceable": True
        end_time = None
        for sub_entry in reports["objects"][reports["objects"].index(entry):]:
            if sub_entry["is_serviceable"] == True:
                end_time = sub_entry["created_at"]
                ending_report = sub_entry["report_uuid"]
                break

        if end_time is not None and start_time is not None:
            end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            start = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            total_hrs = end - start

            days = total_hrs.days
            hours, remainder = divmod(total_hrs.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            downtime = f"{days} days, {hours:02d}:{minutes:02d}:{seconds:02d}"

            # Accumulate downtime duration to the total_downtime
            total_downtime += total_hrs

        # Step 6: Append the downtime report to the list
        downtime_reports.append({
            "start": {
                "starting_report": starting_report,
                "datetime": start_time
            },
            "end": {
                "ending_report": ending_report if end_time else None,
                "datetime": end_time if end_time else str(datetime.datetime.now())
            },
            "downtime": str(downtime),
        })

        ignore_next_false = True  # Ignore consecutive instances of ["is_serviceable"] == False

# Step 7: Convert total_downtime to the desired format
total_days = total_downtime.days
total_hours, total_remainder = divmod(total_downtime.seconds, 3600)
total_minutes, total_seconds = divmod(total_remainder, 60)

total_downtime_formatted = f"{total_days} days, {total_hours:02d}:{total_minutes:02d}:{total_seconds:02d}"

# Step 8: Add total_downtime to the last downtime report
downtime_reports.append({"total_downtime": total_downtime_formatted})

# for report in downtime_reports:
#   print(report)

print(downtime_reports)

print({"downtime_report_count": len(downtime_reports)-1})