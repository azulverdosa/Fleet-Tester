import { reverse } from './data';

const anotherUuid = '2ffd6494-68ae-4b4b-8a54-d2b36181b44f';
const otherUuid = '0cc18e59-ee6a-4b0b-974a-2998686af408';
const bmw1Uuid = 'e844b8b3-f627-462b-9a1d-514a7b3f0831';
const multihogUuid = '3ddf5d06-1323-4924-a038-203344e7d4c9';

const getMilliseconds = (dateStr = Date()) => new Date(dateStr).getTime();

// this filter is not the one to use in real life
// throwaway code: mocks missing database
const filtered = reverse().filter(({ createdAt, vehicleUuid }) => {
  return vehicleUuid === bmw1Uuid;
});
// end of throwaway

// console.log('filtered :>> ', filtered);

const results = filtered.reduce(
  (previousStatus, report, index, reports) => {
    const isLastReportInRange = index === reports.length - 1;

    if (
      previousStatus.start &&
      // only "rto = true" ends downtime
      report.isRTOInspectionRequired
    ) {
      // was broken and not unsafe anymore
      console.log('fixxd!');
      console.log('ended :>> ', report.createdAt);

      const downtimeMilliSeconds =
        getMilliseconds(report.createdAt) - getMilliseconds(previousStatus.start);
      const downtimeHours = Number((downtimeMilliSeconds / 1000 / 60 / 60).toFixed(2));

      console.log('previousDowntimeHours :>> ', previousStatus.totalHours);
      console.log('downtimeHours :>> ', downtimeHours);

      const newStatus = {
        start: null,
        totalHours: previousStatus.totalHours + downtimeHours,
      };

      // unsafe false and rto false/null
      // (may or not have faults)
      // no start date at submission
      // i.e. changes nothing

      return newStatus;
    } else if (
      report.isUnsafe
      // "rto" always null in this case
    ) {
      if (previousStatus.start) {
        console.log('still unsafe');
      } else {
        console.log('it broke!');
        console.log('start :>> ', report.createdAt);
      }

      const newStatus = {
        start: previousStatus.start || report.createdAt,
        totalHours: previousStatus.totalHours, // problematic
      };

      return newStatus;
    }

    console.log('usable');
    report.isRTOInspectionRequired && console.log('rto required');

    return previousStatus;
  },
  {
    start: null,
    totalHours: 0,
  }
);

console.log('Total Hours :>> ', results.totalHours);
