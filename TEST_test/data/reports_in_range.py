import json
from datetime import datetime as datetime, timedelta, timezone

# reports = {
#     "objects":[
#             {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-01 00:00:00",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-02 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-03 00:00:00",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-05 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-10 00:00:00",
#             "is_serviceable": False
#         },
#                 {
#             "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-14 00:00:00",
#             "is_serviceable": False
#         },
#         # start date Jan 16
#         {
#             "report_uuid": "f93f2f4f-8fff-4c5a-ad22-d9a330e4f8c9",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-18 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "c6215a43-3fec-42b9-824c-f9c397571532",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-05 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "57120477-5f25-4389-a0b1-f0e2b0d93c32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "f022c768-6ecd-45d1-919d-cb0d8c1e6b32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-10 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "ac4f16c7-d19e-4be2-8b2d-01be24f4311f",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-15 00:00:00",
#             "is_serviceable": False
#         },
#         {
#             "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-16 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-18 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-25 00:00:00",
#             "is_serviceable": False
#         },
#         # end date May 28
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-06-08 00:00:00",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-06-18 00:00:00",
#             "is_serviceable": True
#         },
#     ],
# }


# reports = {
#     "objects":[
#         {
#             "report_uuid": "91d8134b-163c-4cbd-b4ca-075804e97892",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2022-08-11 18:47:55",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "a58eb3d9-e0da-4276-be74-941bd1fcdaad",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-05 21:08:12",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "d71238fd-877c-4c2b-8d5d-9d3da1f160ae",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-10 18:50:30",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "f93f2f4f-8fff-4c5a-ad22-d9a330e4f8c9",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-01-18 18:25:23",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "c6215a43-3fec-42b9-824c-f9c397571532",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 16:49:53",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "57120477-5f25-4389-a0b1-f0e2b0d93c32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 16:50:59",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "f022c768-6ecd-45d1-919d-cb0d8c1e6b32",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 16:52:19",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "ac4f16c7-d19e-4be2-8b2d-01be24f4311f",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-03-07 21:20:32",
#             "is_serviceable": None
#         },
#         {
#             "report_uuid": "a49a9df4-abad-46e8-beca-a849bd11d9b0",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-16 17:39:55",
#             "is_serviceable": True
#         },
#         {
#             "report_uuid": "34946cc3-b051-4b95-b4f3-b6a903c6f7b3",
#             "vehicle_uuid": "c3916926-e3d7-411f-8750-b518aa86ce0f",
#             "vehicle_name": "A1",
#             "created_at": "2023-05-16 17:40:41",
#             "is_serviceable": None
#         }
#     ],

# }


# reports = [
#         {   "report_uuid": "11/16 start-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-11-16 17:40:41",
#             "is_serviceable": False
#         },
#         {    "report_uuid": "23/2 end-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-02-07 16:50:59",
#             "is_serviceable": True
#         },
#         {    "report_uuid": "8/11 start-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2022-08-11 18:47:55",
#             "is_serviceable": False
#         },
#         {    "report_uuid": "5/16 end-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-05-16 17:39:55",
#             "is_serviceable": True
#         },
#         {    "report_uuid": "1/5 end-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-01-05 21:08:12",
#             "is_serviceable": True
#         },
#         {    "report_uuid": "None",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-09-07 21:20:32",
#             "is_serviceable": None
#         },
#         {    "report_uuid": "3/17 start-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-03-17 16:49:53",
#             "is_serviceable": False
#         },
#         {    "report_uuid": "1/10 end-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-01-10 18:50:30",
#             "is_serviceable": True
#         },
#         {    "report_uuid": "3/7 end-report",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-03-07 16:52:19",
#             "is_serviceable": True
#         },
#         {    "report_uuid": "none",
#             "vehicle_uuid": "58a20a4e-f1dc-44f4-a72f-af8c79616208",
#             "vehicle_name": "A4",
#             "created_at": "2023-01-18 18:25:23",
#             "is_serviceable": None
#         }
#     ]

reports = [
    {
        'report_uuid': '7911a079-e16f-41ab-8c79-f8a6fa93ec52',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-24 19:43:09',
        'is_serviceable': None,
    },
    {
        'report_uuid': '4bf8ac97-f21b-4852-8ca5-a4c7d3b11d40',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-24 19:49:25',
        'is_serviceable': True,
    },
    {
        'report_uuid': '6ba7f868-fbdd-41d0-ae2e-eb828784664d',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-24 19:49:56',
        'is_serviceable': None,
    },
    {
        'report_uuid': '7978bc80-d585-41fb-b40b-26dbb936f295',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-24 20:40:40',
        'is_serviceable': False,
    },
    {
        'report_uuid': 'df600969-3443-425b-8c80-4691d6c82fde',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-24 20:41:56',
        'is_serviceable': None,
    },
    {
        'report_uuid': 'b034683e-cd3f-4b25-b1d4-8728359404b6',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-27 13:54:35',
        'is_serviceable': None,
    },
    {
        'report_uuid': '61958387-59c4-45a5-bbed-55789f42c476',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-27 14:33:01',
        'is_serviceable': True,
    },
    {
        'report_uuid': '161c719c-42a6-4286-923c-dcaaa2fbf91f',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-27 14:35:12',
        'is_serviceable': True,
    },
    {
        'report_uuid': '4d6dadf1-8501-44a7-be9d-f63773c82d0d',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-27 15:03:47',
        'is_serviceable': True,
    },
    {
        'report_uuid': '54912688-91ac-49d6-911a-899b7c99cb33',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-27 15:04:23',
        'is_serviceable': None,
    },
    {
        'report_uuid': 'fd27c4f5-6ae3-4237-a84b-0d5565438386',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:25:47',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'c88fd2ac-2d43-4bff-b5cc-3321945319bb',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:28:09',
        'is_serviceable': True,
    },
    {
        'report_uuid': '5ebf8b6e-c336-446e-94cd-7aa606bea752',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:28:52',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'b15b7a9a-f78f-42b3-905e-806e37ec2d4e',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:33:43',
        'is_serviceable': False,
    },
    {
        'report_uuid': '904b6392-7f3e-4e10-bf3e-9032128d29db',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:34:19',
        'is_serviceable': None,
    },
    {
        'report_uuid': 'ab043cf3-d950-4fbc-9904-c0ac3b47952e',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:35:31',
        'is_serviceable': None,
    },
    {
        'report_uuid': '3572065f-68c3-4592-a182-08fce7790928',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:43:09',
        'is_serviceable': False,
    },
    {
        'report_uuid': '03f0e6bc-b0c5-4471-91e6-1bdf2650ed07',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 14:46:19',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'f9f010d6-a263-49d6-b1ea-669a60f62fa3',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 15:18:04',
        'is_serviceable': None,
    },
    {
        'report_uuid': '7a2a865a-78ba-4c9c-95f7-eca4b0a53534',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 15:18:55',
        'is_serviceable': True,
    },
    {
        'report_uuid': '938ead39-94cb-4d72-9c7f-fa91be2e1d76',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 15:19:33',
        'is_serviceable': None,
    },
    {
        'report_uuid': 'fdb67aca-695d-440a-8be6-6b75bc6ae4d6',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 15:20:39',
        'is_serviceable': None,
    },
    {
        'report_uuid': '768dbee8-fe39-437e-bb96-1f9094f61081',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 15:21:12',
        'is_serviceable': None,
    },
    {
        'report_uuid': '9f8d851f-9468-44fc-8bbd-260d642be94a',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-05-28 15:44:00',
        'is_serviceable': None,
    },
    {
        'report_uuid': '94ebb136-1f37-4c17-818e-c42ba3eea9e0',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:10:45',
        'is_serviceable': False,
    },
    {
        'report_uuid': '663f3b20-76f5-4bce-a868-ced17fbb0e4a',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:16:20',
        'is_serviceable': False,
    },
    {
        'report_uuid': '36a56fbd-131d-4c72-b811-9fcc7396cf9a',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:18:40',
        'is_serviceable': False,
    },
    {
        'report_uuid': 'f15e116f-f2ea-4f5b-8428-13e446f5917b',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:19:37',
        'is_serviceable': False,
    },
    {
        'report_uuid': 'b0fa0803-956e-41d5-85c4-85bbf96b882e',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:22:39',
        'is_serviceable': False,
    },
    {
        'report_uuid': 'f5f7d1fa-4948-4d87-8dee-01e7d036d6b2',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:34:36',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'be52c219-5a4f-4150-bf77-269384c73518',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:35:18',
        'is_serviceable': True,
    },
    {
        'report_uuid': '8c33f928-de34-425c-b3ea-34d2fe237b5f',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:36:16',
        'is_serviceable': True,
    },
    {
        'report_uuid': '699bb40d-e5ba-4d4a-ba9e-43fdfdbc03d0',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-20 15:43:46',
        'is_serviceable': False,
    },
    {
        'report_uuid': '42f53566-8585-41a4-800b-3900ee0ff348',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-06-24 14:36:25',
        'is_serviceable': False,
    },
    {
        'report_uuid': 'd7bb909b-947b-4e00-b36f-22dd62dad005',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-10-02 16:57:10',
        'is_serviceable': False,
    },
    {
        'report_uuid': 'bbef46bf-8934-480e-9261-60466c546e97',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-10-02 17:01:49',
        'is_serviceable': False,
    },
    {
        'report_uuid': '1f088226-c78b-45b5-9b0d-5c1470051005',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-10-02 17:06:09',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'f0301cc9-f46c-4be2-b592-3f30f94ac6f8',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-10-02 17:06:19',
        'is_serviceable': False,
    },
    {
        'report_uuid': '7cc10fea-db52-41f8-8a6c-8327d0d67c0c',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-11-11 16:55:49',
        'is_serviceable': None,
    },
    {
        'report_uuid': '02982816-8e62-4b93-97e3-4011922f65df',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-11-11 16:56:16',
        'is_serviceable': True,
    },
    {
        'report_uuid': '27a3f472-fe7c-4dd8-9425-43f922445c79',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-11-11 18:12:36',
        'is_serviceable': True,
    },
    {
        'report_uuid': '968ff47d-3b4c-4c00-9743-bf47f3b18956',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-11-11 18:19:08',
        'is_serviceable': None,
    },
    {
        'report_uuid': 'cf50b6dd-2da5-45a1-bd0f-46a29aa0ae8d',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2019-12-04 17:05:35',
        'is_serviceable': None,
    },
    {
        'report_uuid': '8626bcef-49f0-4c7d-b7a8-95c63c17c6dd',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2020-01-14 21:32:45',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'f937f004-c2f7-4e9f-b414-66aa49a6f286',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2020-04-07 17:39:03',
        'is_serviceable': None,
    },
    {
        'report_uuid': '942baa32-8e74-42a3-9f17-7338855f370b',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2020-04-09 14:49:52',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'cacac087-f796-427e-9db5-c282c449972b',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2020-04-09 16:19:46',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'b9ab7a5a-5755-46dc-a8f3-dd06955c3941',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2020-04-09 17:18:33',
        'is_serviceable': True,
    },
    {
        'report_uuid': '6edd5360-0eea-42aa-8a12-a636ed6f89d5',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2020-04-09 18:21:59',
        'is_serviceable': True,
    },
    {
        'report_uuid': 'ddc82dae-ef17-4b58-b557-1015b71c935d',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2020-04-09 18:27:03',
        'is_serviceable': True,
    },
    # {
    #     'report_uuid': 'beeecfd5-d847-439e-9f06-40d4dd85b992',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2020-04-09 18:27:56',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': '9368f677-e1ae-440d-9d6b-901e6f2a69b2',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2020-04-09 18:29:05',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': 'd5d7bfd3-ea63-4bbf-a457-542b7e794e18',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2020-04-09 18:29:26',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': '1bd66bc6-42a7-4e36-b834-ed079de85e07',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2020-04-09 18:29:37',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': '35a0097a-b81d-47a9-96b8-01f36520df29',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2021-01-28 22:30:36',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': 'c8712c7d-1df9-49a1-99dd-6e7dd8da78b4',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-02-01 19:46:56',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '29e9f8ba-7295-42b1-abeb-5f270bd4cd9a',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-02-01 20:03:53',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': 'dffd09f5-b67a-48b4-9ea8-9e8583d62e21',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-02-01 23:00:42',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '7532ee33-c0bd-4ac8-8f02-1af7c4b71cd4',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-03-02 00:11:06',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '6737bf3f-8cd1-4b7f-9ea1-5819b716e948',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-13 21:07:23',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '7c219078-34e9-4fac-afef-59f6d9a24938',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 14:00:16',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': 'e24ffb01-def2-42c3-8434-f235584542a1',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 16:03:41',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '3d1c67f1-5a07-487b-9a76-313ee409d862',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 16:04:07',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '346c5ec7-1a3a-46aa-a94a-197320baf638',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 16:08:02',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': 'fe626147-bcf9-4c85-ac37-2b1c060158c9',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 16:28:56',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': '54b90a27-4709-4134-b5f1-5f7aa81d8cee',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 16:55:12',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': '555ef75b-b859-4027-b77e-73ff9d1a7f2d',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 17:00:49',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': 'b6909cb8-ddcb-4414-9832-1e8f88e188d2',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 17:04:40',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '4da34cb8-759a-4d69-9499-a2d6b8576ba9',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 17:08:05',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '88ec90da-02f6-4728-931b-30cd2e9b7fd2',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 17:52:40',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '6e0a418e-c24a-4163-bcff-7ea423bdda05',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 17:53:15',
    #     'is_serviceable': True,
    # },
    # {
    #     'report_uuid': '849f7589-3268-4dd4-b532-cb0cdc45bc82',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 17:54:00',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': 'b7f06a39-efa7-4039-8362-7925ed824608',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-14 17:59:34',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': '6c1dc8be-aa27-4ba1-bc02-8cc431eae99f',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-04-19 20:39:43',
    #     'is_serviceable': None,
    # },
    # {
    #     'report_uuid': 'ce9c5c4e-dc88-4000-b188-f94640c60ac9',
    #     'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
    #     'vehicle_name': 'Left Blower 188',
    #     'vehicle_asset_number': '10-1014',
    #     'created_at': '2022-06-06 17:39:16',
    #     'is_serviceable': True,
    # },
    {
        'report_uuid': '4b65a506-4285-4406-bf1e-f71a7e80ea09',
        'vehicle_uuid': '1dc9f8da-9818-446d-ba37-9cca161d22d0',
        'vehicle_name': 'Left Blower 188',
        'vehicle_asset_number': '10-1014',
        'created_at': '2022-06-08 18:56:12',
        'is_serviceable': False,
    },
]

range_start = datetime.strptime("2023-01-16", '%Y-%m-%d')
range_end = datetime.strptime("2012-01-01", '%Y-%m-%d') 


def filter_reports_in_range(reports, range_start, range_end):
    sorted_reports = sorted(reports, key=lambda x: x["created_at"])

    reports_in_range = []  
    filtered_reports_for_calc = [] 

    for index, report in enumerate(sorted_reports):
        report_date = datetime.strptime(report["created_at"], "%Y-%m-%d %H:%M:%S")
        
        if range_start <= report_date <= range_end:
            reports_in_range.append(report)

            if len(reports_in_range) == 1:
                index_for_first_filtered_entry = index

    if len(reports_in_range) < 1:
        print("no reports in range")
        return

    last_report_in_range = reports_in_range[-1]

    if last_report_in_range["is_serviceable"] is False:
        print("dowtime ends after range")

        last_report_for_calc = {
            "report_uuid": "downtime ends after range",
            "vehicle_uuid": last_report_in_range["vehicle_uuid"],
            "vehicle_name": last_report_in_range["vehicle_name"],
            "created_at": range_end.strftime("%Y-%m-%d %H:%M:%S"),
            "is_serviceable": True
        }

        reports_in_range.append(last_report_for_calc)
    else:
        filtered_reports_for_calc = reports_in_range

    if index_for_first_filtered_entry:
        report_before_date_range = sorted_reports[index_for_first_filtered_entry - 1]
        serviceable_before_range = report_before_date_range["is_serviceable"]

        if serviceable_before_range is True or serviceable_before_range is None:
            print("dowtime starts in range")
            filtered_reports_for_calc = reports_in_range

        elif serviceable_before_range is False:
            print("dowtime starts before range")
            first_report_for_calc = {
            "report_uuid": "downtime starts before range",
            "vehicle_uuid": report_before_date_range["vehicle_uuid"],
            "vehicle_name": report_before_date_range["vehicle_name"],
            # "vehicle_asset_number": report_before_date_range["vehicle_asset_number"],
            "created_at": range_start.strftime("%Y-%m-%d %H:%M:%S"),
            "is_serviceable": serviceable_before_range
        }

            filtered_reports_for_calc = [first_report_for_calc] + reports_in_range
    else:
        print("no inspections prior to date range")

    return filtered_reports_for_calc


reports_for_calc = filter_reports_in_range(reports, range_start, range_end)

print("reports_for_calc =",reports_for_calc)


