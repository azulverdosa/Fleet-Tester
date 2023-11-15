--------------Javascript translated logic below by Poe ----------------------------------------------------------------------

from report_data import data
from datetime import datetime

another_uuid = '2ffd6494-68ae-4b4b-8a54-d2b36181b44f'
other_uuid = '0cc18e59-ee6a-4b0b-974a-2998686af408'
bmw1_uuid = 'e844b8b3-f627-462b-9a1d-514a7b3f0831'
multihog_uuid = '3ddf5d06-1323-4924-a038-203344e7d4c9'

def get_milliseconds(date_str=None):
    date_str = date_str or datetime.now().isoformat()
    return int(datetime.fromisoformat(date_str).timestamp() * 1000)

# this filter is not the one to use in real life
# throwaway code: mocks missing database
filtered = list(filter(lambda x: x['vehicleUuid'] == bmw1_uuid, reversed(data["objects"])))
# end of throwaway

results = {
    'start': None,
    'totalHours': 0
}

for index, report in enumerate(filtered):
    is_last_report_in_range = index == len(filtered) - 1

    if results['start'] is not None and report['isRTOInspectionRequired']:
        print('fixxd!')
        print('ended :>>', report['createdAt'])

        downtime_milliseconds = get_milliseconds(report['createdAt']) - get_milliseconds(results['start'])
        downtime_hours = round(downtime_milliseconds / 1000 / 60 / 60, 2)

        print('previousDowntimeHours :>>', results['totalHours'])
        print('downtimeHours :>>', downtime_hours)

        results['totalHours'] += downtime_hours
        results['start'] = None

    elif report['isUnsafe']:
        if results['start'] is not None:
            print('still unsafe')
        else:
            print('it broke!')
            print('start :>>', report['createdAt'])
            results['start'] = report['createdAt']

    print('usable')
    if report['isRTOInspectionRequired']:
        print('rto required')

print('Total Hours :>>', results['totalHours'])