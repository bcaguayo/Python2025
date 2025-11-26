import requests
import json

contact = 443877167298

# Bearer token
AUTH = ""

# Get auth from /Secret/auth.py
with open('Secret/auth.txt') as f:
    AUTH = f.read().strip()

# Set the API endpoints and headers
endpoint = f'https://api.hubapi.com/engagements/v1/engagements/associated/contact/{contact}/paged'
headers = {"Authorization" : f"Bearer {AUTH}"}

# Make a GET request to the API
response = requests.get(endpoint, headers=headers)

# Parse the JSON data from the response
data = response.json()

print(json.dumps(data, indent=2))

# Loop through the contacts and print their information
# for contact in data["contacts"]:
#     print(json.dumps(contact, indent=2))
    # stc = "'" + str(contact) + "'"
    # print(json.dumps(json.loads(stc), indent=2))