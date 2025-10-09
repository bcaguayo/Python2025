import requests
import json

# Set the API endpoints and headers
url = "https://api.hubapi.com/crm/v3/objects/deals/321820069050"

querystring = {"properties":"original_deal"}

headers = {"Authorization" : "Bearer pat-eu1-c8242757-5a04-4df6-9acc-317da1018a7f"}

# Make a GET request to the API
response = requests.get(url, headers=headers, params=querystring)

# Parse the JSON data from the response
data = response.json()

print(json.dumps(data, indent=2))

# Loop through the contacts and print their information
# for contact in data["contacts"]:
#     print(json.dumps(contact, indent=2))