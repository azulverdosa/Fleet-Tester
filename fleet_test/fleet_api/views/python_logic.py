from vammas166 import reports
import datetime

# NOTE - the provided code will only consider the duration when the "is_serviceable" value is False. It will not include the duration when "is_serviceable" is None.
# In the given code, the if not report["is_serviceable"] condition checks if the value of "is_serviceable" is False. If it is False, it proceeds to calculate the duration.
# If "is_serviceable" is None, it will be treated as a truthy value and will not satisfy the condition if not report["is_serviceable"]. Therefore, the code will not calculate the duration for such cases.

# Sort the reports chronologically based on the "created_at" timestamp. This step ensures that the reports are in ascending order based on time.

# Initialize variables to track the start and end timestamps for the "is_serviceable": false duration, as well as the total duration.

# Iterate through the sorted reports and perform the following steps for each report:

    # Check if the "is_serviceable" value is false.
    # If it is false, set the start timestamp if it has not been set already.
    # If it is true and the start timestamp has been set, calculate the duration by subtracting the start timestamp from the current report's timestamp. Add this duration to the total duration.
    # Reset the start timestamp to None.

# After iterating through all the reports, if the start timestamp is not None (indicating that the final report had "is_serviceable": false), calculate the duration from the start timestamp to the end of the time period (or the current time). Add this duration to the total duration.

# The total duration represents the duration for which the vehicle had "is_serviceable": false.

# START LOGIC ---->
reports = reports["dtreports"]

# Sort the reports 
# NOTE The sort() method sorts the list in-place and does not return a new sorted list -- do not set reports.sort() to a variable
reports.sort(key=lambda x: x["created_at (strftime)"])

# Initialize variables 
start_timestamp = None
total_duration = datetime.timedelta()

# Iterate 
for report in reports:
    # Check if the "is_serviceable" value is false.
    # NOTE - the code will only consider the duration when the "is_serviceable" value is False. It will not include the duration when "is_serviceable" is None.
    if not report["is_serviceable"]:
        # If it is false, set the start timestamp if it has not been set already.
        if start_timestamp is None:
            start_timestamp = datetime.datetime.strptime(report["created_at (strftime)"], "%Y-%m-%d %H:%M:%S")
    elif start_timestamp is not None:
        # If it is true and the start timestamp has been set, calculate the duration by subtracting the start timestamp from the current report's timestamp. Add this duration to the total duration.
        current_timestamp = datetime.datetime.strptime(report["created_at (strftime)"], "%Y-%m-%d %H:%M:%S")
        duration = current_timestamp - start_timestamp
        total_duration += duration
        # Reset the start timestamp to None.
        start_timestamp = None

# If the start timestamp is not None - check if the last report had "is_serviceable": false
if start_timestamp is not None:
    current_timestamp = datetime.datetime.now()
    duration = current_timestamp - start_timestamp
    total_duration += duration

# The total duration 
print("Total duration with is_serviceable = False:", total_duration)


# TODO return should be:
# Total duration with is_serviceable=False: 170 days, 0:35:03.633941
# 
# This indicates that the vehicle had an "is_serviceable": false duration of 9 days, 1 hour, 59 minutes, and 14 seconds.