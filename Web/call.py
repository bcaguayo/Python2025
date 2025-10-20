import requests

AUTH = ""
# Get auth from /Secret/auth.py
with open('/Secret/auth.py') as f:
    AUTH = f.read().strip()

# Set the API endpoint
# url = "https://api.hubapi.com/crm/v3/objects/contacts"
url = "https://api.hubapi.com/engagements/v1/engagements"

# Set the request headers
headers = {
   "Content-Type": "application/json",
   "Authorization" : f"Bearer {AUTH}"
}

# Set the contact information
call = {
  "engagement": {
    "active": True,
    "type": "CALL"
  },
  "metadata": {
    "toNumber": "+447709181253",
    "fromNumber": "+440987654321",
    "hs_call_direction": "inbound",
    "hubspot_owner_id": "51545623",
    "status": "COMPLETED",
    "durationMilliseconds": 300000,
    "recordingUrl": "https://example.com/recording",
    "body": (
      "<b>Direction:</b> INBOUND: <b>Note:</b> Test call: <b>Campaign:</b> Test Campaign"
    ),
    "title": "Test Call"
  }   
}

# Send the request
response = requests.post(url, json=call, headers=headers)

if response.status_code == 201 or response.status_code == 200:
   print("Call Created Successfully")
else:
   print("Failed To Create Call")