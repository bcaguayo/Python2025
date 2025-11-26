import requests

AUTH = ""
# Get auth from /Secret/auth.py
with open('Secret/auth.txt') as f:
    AUTH = f.read().strip()

# Set the API endpoint
url = "https://api.hubapi.com/crm/v3/objects/calls"

# Set the request headers
headers = {
   "Content-Type": "application/json",
   "Authorization" : f"Bearer {AUTH}"
}

# Set the contact information
call = {
  "associations": [
    {
      "to": {
        "id": "531556309234"
      },
      "types": [
        {
          "associationCategory": "HUBSPOT_DEFINED",
          "associationTypeId": 194
        }
      ]
    }
  ],
  "engagement": {
    "ownerId": "30225842"
  },
  "interactions": {},
  "metadata": {
    "disposition": "f240bbac-87c9-4f6e-bf70-924b57d47db7",
    "durationMilliseconds": "",
    "status": "IN_PROGRESS"
  },
  "properties": {
    "hs_call_body": "TEST INTEGRATION CALL",
    "hs_call_direction": "INBOUND",
    "hs_call_duration": 274,
    "hs_call_recording_url": "https://consultationclaims-cxm-api.uk.connexone.cloud/voice/recording/f57e4721-8b9b-4779-b5c7-27e64c9f84fd",
    "hs_call_title": "IntegrationTest",
    "hs_call_to_number": "+447842132334",
    "hs_timestamp": "2025-11-14T10:43:45.373998+00:00",
    "hubspot_owner_id": "76831781"
  }
}

# Send the request
response = requests.post(url, json=call, headers=headers)

status = response.status_code
body = response.text

if response.status_code == 201 or response.status_code == 200:
   print("Call Created Successfully")
else:
   print("Failed To Create Call")

print(body)