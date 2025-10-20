import requests
import json

AUTH = ""
# Get auth from /Secret/auth.py
with open('/Secret/auth.py') as f:
    AUTH = f.read().strip()

headers = {"Authorization" : f"Bearer {AUTH}"}

# Set the API endpoints and headers
url = "https://api.hubapi.com/crm/v3/objects/deals/321820069050"

querystring = {"properties":"original_deal"}

# Make a GET request to the API
response = requests.get(url, headers=headers, params=querystring)

# Parse the JSON data from the response
data = response.json()

print(json.dumps(data, indent=2))

# Loop through the contacts and print their information
# for contact in data["contacts"]:
#     print(json.dumps(contact, indent=2))