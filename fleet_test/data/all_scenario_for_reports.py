import json
from datetime import datetime as datetime, timedelta, timezone

reports = [
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-01-28 14:46:19',
    "is_serviceable": True,
  },
  {
    "hours": 3,
    "kilometers": 8765,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-02-18 14:46:19',
    "is_serviceable": True,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-03-08 14:46:19',
    "is_serviceable": True,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-04-02 14:46:19',
    "is_serviceable": False,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-05-12 14:46:19',
    "is_serviceable": False,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-06-23 14:46:19',
    "is_serviceable": None,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-07-11 14:46:19',
    "is_serviceable": True,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-08-30 14:46:19',
    "is_serviceable": False,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-09-09 14:46:19',
    "is_serviceable": None,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-10-31 14:46:19',
    "is_serviceable": True,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-11-16 14:46:19',
    "is_serviceable": False,
  },
  {
    "hours": None,
    "kilometers": None,
    "isUnsafe": False,
    "isRecurrent": False,
    "vehicle_uuid": '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    "vehicle_name": 'Left Blower 188',
    "created_at": '2023-12-19 14:46:19',
    "is_serviceable": True,
  },
]


range_start = "2023-08-01"
range_end = "2023-09-30"


def filter_reports_in_range(reports, range_start, range_end):
    sorted_reports = sorted(reports, key=lambda x: x["created_at"])
    range_start_converted = datetime.strptime(range_start, '%Y-%m-%d')
    range_end_converted = datetime.strptime(range_end, '%Y-%m-%d')
    reports_in_range = []  
    serviceable_status_for_first_report_in_range = None
    serviceable_status_for_last_report_in_range = None
    first_report_in_range = None
    last_report_in_range = None
    single_report_in_range = None
    previous_report_before_range_start = None
    serviceable_status_before_date_range = None
    filtered_reports_for_calc = []  

    for report in sorted_reports:
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")
        
        if range_start_converted <= report_date <= range_end_converted:
            reports_in_range.append(report)

    for report in reversed(sorted_reports):
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")

        if report_date > range_start_converted:
            continue

        if report_date < range_start_converted:
            previous_report_before_range_start = report
            serviceable_status_before_date_range = previous_report_before_range_start["is_serviceable"]
            break
        
    if len(reports_in_range) == 0:
        print("0 reports_in_range")
        print("previous_report_before_range_start", previous_report_before_range_start)

        if serviceable_status_before_date_range in [True, None]:
            print("no reports AND no downtime")

            filtered_reports_for_calc = reports_in_range

        elif serviceable_status_before_date_range is False:
            print("no reports BUT downtime starts before date range and ends after date range - DT is whole date range")

            new_downtime_start_report = {
                "report_uuid": "DOWNTIME STARTS BEFORE RANGE - downtime is entire date range",
                "vehicle_uuid": single_report_in_range["vehicle_uuid"],
                "vehicle_name": single_report_in_range["vehicle_name"],
                "created_at": range_start_converted,
                "is_serviceable": False
                }
            
            new_downtime_end_report = {
                "report_uuid": "DOWNTIME ENDS AFTER RANGE - downtime is entire date range",
                "vehicle_uuid": single_report_in_range["vehicle_uuid"],
                "vehicle_name": single_report_in_range["vehicle_name"],
                "created_at": range_end_converted,
                "is_serviceable": True
                }
            
            filtered_reports_for_calc = [new_downtime_start_report, new_downtime_end_report]


    if len(reports_in_range) == 1:
        print("1 report in_range", reports_in_range)
        print("previous_report_before_range_start", previous_report_before_range_start)

        serviceable_status_for_single_report = reports_in_range[0]["is_serviceable"]

        if serviceable_status_before_date_range is False and serviceable_status_for_single_report in [True, None] :
            print("downtime starts before range & single report is DT END")

            new_downtime_start_report = {
                "report_uuid": "DOWNTIME STARTS BEFORE RANGE",
                "vehicle_uuid": single_report_in_range["vehicle_uuid"],
                "vehicle_name": single_report_in_range["vehicle_name"],
                "created_at": range_start_converted,
                "is_serviceable": False
                }

            filtered_reports_for_calc = new_downtime_start_report + reports_in_range

        elif serviceable_status_before_date_range in [True, None] and serviceable_status_for_single_report in [True, None]:
            print("NO DT withing range")

            filtered_reports_for_calc = reports_in_range #remover report for ease later?

        elif serviceable_status_before_date_range in [True, None] and serviceable_status_for_single_report is False:
            print("single report is DT START & downtime ends after range")

            new_downtime_end_report = {
                "report_uuid": "DOWNTIME ENDS AFTER RANGE",
                "vehicle_uuid": single_report_in_range["vehicle_uuid"],
                "vehicle_name": single_report_in_range["vehicle_name"],
                "created_at": range_end_converted,
                "is_serviceable": True
                }
            
            filtered_reports_for_calc = reports_in_range + [new_downtime_end_report]

        elif serviceable_status_before_date_range is False and serviceable_status_for_single_report is False:
            print("downtime starts before range, ends after range & single report is MIDDLE of downtime")

            new_downtime_start_report = {
                "report_uuid": "DOWNTIME STARTS BEFORE RANGE - downtime is entire date range",
                "vehicle_uuid": single_report_in_range["vehicle_uuid"],
                "vehicle_name": single_report_in_range["vehicle_name"],
                "created_at": range_start_converted,
                "is_serviceable": False
                }

            new_downtime_end_report = {
                "report_uuid": "DOWNTIME ENDS AFTER RANGE - downtime is entire date range",
                "vehicle_uuid": single_report_in_range["vehicle_uuid"],
                "vehicle_name": single_report_in_range["vehicle_name"],
                "created_at": range_end_converted,
                "is_serviceable": True
                }
            
            filtered_reports_for_calc = [new_downtime_start_report] + reports_in_range + [new_downtime_end_report]


    if len(reports_in_range) > 1:
        print(">1 reports_in_range") #, reports_in_range)
        print("before", len(reports_in_range))
        first_report_in_range = reports_in_range[0]
        last_report_in_range = reports_in_range[-1]
        serviceable_status_for_first_report_in_range = first_report_in_range["is_serviceable"]
        serviceable_status_for_last_report_in_range = last_report_in_range["is_serviceable"]

        is_serviceable_before_date_range = serviceable_status_before_date_range in [True, None]
        is_not_serviceable_before_date_range = not serviceable_status_before_date_range

        is_serviceable_at_first_report_within_date_range = serviceable_status_for_first_report_in_range in [True, None]
        is_not_serviceable_at_first_report_within_date_range = not serviceable_status_for_first_report_in_range

        is_serviceable_at_last_report_within_date_range = serviceable_status_for_last_report_in_range in [True, None]
        is_not_serviceable_at_last_report_within_date_range = not serviceable_status_for_last_report_in_range

        # A
        downtime_stars_within_date_range_and_ends_after_date_range = (is_serviceable_before_date_range and is_serviceable_at_first_report_within_date_range and is_not_serviceable_at_last_report_within_date_range) or (is_serviceable_before_date_range and is_not_serviceable_at_first_report_within_date_range and is_not_serviceable_at_last_report_within_date_range)
        
        # B
        downtime_starts_before_date_range_and_ends_after_date_range = (is_not_serviceable_before_date_range and is_serviceable_at_first_report_within_date_range and is_not_serviceable_at_last_report_within_date_range) or (is_not_serviceable_before_date_range and is_not_serviceable_at_first_report_within_date_range and is_not_serviceable_at_last_report_within_date_range)

        # C
        downtime_starts_and_ends_within_date_range = (is_serviceable_before_date_range and is_serviceable_at_first_report_within_date_range and is_serviceable_at_last_report_within_date_range) or (is_serviceable_before_date_range and is_not_serviceable_at_first_report_within_date_range and is_serviceable_at_last_report_within_date_range) 
        
        # D
        downtime_starts_before_date_range_and_ends_within_date_range = (is_not_serviceable_before_date_range and is_serviceable_at_first_report_within_date_range and is_serviceable_at_last_report_within_date_range) or (is_not_serviceable_before_date_range and is_not_serviceable_at_first_report_within_date_range and is_not_serviceable_at_last_report_within_date_range)

        if downtime_stars_within_date_range_and_ends_after_date_range:
            print("downtime_stars_within_date_range_and_ends_after_date_range", downtime_stars_within_date_range_and_ends_after_date_range)
            new_downtime_end_report = {
                "report_uuid": "DOWNTIME ENDS AFTER RANGE",
                "vehicle_uuid": first_report_in_range["vehicle_uuid"],
                "vehicle_name": first_report_in_range["vehicle_name"],
                "created_at": range_end_converted,
                "is_serviceable": True
            }

            filtered_reports_for_calc = reports_in_range + [new_downtime_end_report]

            print("after", len(filtered_reports_for_calc))

        elif downtime_starts_before_date_range_and_ends_after_date_range:
            print("downtime_starts_before_date_range_and_ends_after_date_range", downtime_starts_before_date_range_and_ends_after_date_range)  
            new_downtime_start_report = {
                "report_uuid": "DOWNTIME STARTS BEFORE RANGE - downtime is entire date range",
                "vehicle_uuid": first_report_in_range["vehicle_uuid"],
                "vehicle_name": first_report_in_range["vehicle_name"],
                "created_at": range_start_converted,
                "is_serviceable": False
            }

            new_downtime_end_report = {
                "report_uuid": "DOWNTIME ENDS AFTER RANGE - downtime is entire date range",
                "vehicle_uuid": first_report_in_range["vehicle_uuid"],
                "vehicle_name": first_report_in_range["vehicle_name"],
                "created_at": range_end_converted,
                "is_serviceable": True
            }

            filtered_reports_for_calc = [new_downtime_start_report] + reports_in_range + [new_downtime_end_report]

        elif downtime_starts_before_date_range_and_ends_within_date_range:
            print("downtime_starts_before_date_range_and_ends_within_date_range", downtime_starts_before_date_range_and_ends_within_date_range)
            new_downtime_start_report = {
                "report_uuid": "DOWNTIME STARTS BEFORE RANGE",
                "vehicle_uuid": first_report_in_range["vehicle_uuid"],
                "vehicle_name": first_report_in_range["vehicle_name"],
                "created_at": range_start_converted,
                "is_serviceable": False
            }

            filtered_reports_for_calc = new_downtime_start_report + reports_in_range

        elif downtime_starts_and_ends_within_date_range:
            print("downtime_starts_and_ends_within_date_range - no adjustments", downtime_starts_and_ends_within_date_range)
            
            filtered_reports_for_calc = reports_in_range


    return filtered_reports_for_calc

reports_for_calc = filter_reports_in_range(reports, range_start, range_end)

print("reports_for_calc =",reports_for_calc)


def filter_report_data(reports):
    filtered_reports = []

    for report in reports:
        filtered_report = {
            'report_uuid': report.get('report_uuid'),
            'vehicle_uuid': report.get('vehicle_uuid'),
            'vehicle_name': report.get('vehicle_name'),
            'created_at': report.get('created_at'),
            'is_serviceable': report.get('is_serviceable'),
        }
        filtered_reports.append(filtered_report)

    return filtered_reports

filtered_reports_for_calc = filter_report_data(reports_for_calc)

print("filtered_reports_for_calc", filtered_reports_for_calc)