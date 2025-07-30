import requests
import json

# Set the API endpoints and headers
endpoint = "https://api.hubapi.com/contacts/v1/lists/all/contacts/all"
headers = {"Authorization" : "Bearer pat-eu1-c8242757-5a04-4df6-9acc-317da1018a7f"}

# Make a GET request to the API
response = requests.get(endpoint, headers=headers)

# Parse the JSON data from the response
data = response.json()

# Loop through the contacts and print their information
for contact in data["contacts"]:
    print(json.dumps(contact, indent=2))
    # stc = "'" + str(contact) + "'"
    # print(json.dumps(json.loads(stc), indent=2))