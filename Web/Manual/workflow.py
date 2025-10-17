import requests     #type: ignore
import json

contacts = set()

with open("manual.txt", 'r') as f:
    # for each line in the file
    for line in f:
        contacts.add(line.strip())

url = "https://api.hubapi.com/crm/v3/objects/contacts/"

payload = { "properties": {
        "hs_marketable_status": "false"
    } }

headers = {
    "Authorization": "Bearer pat-eu1-c8242757-5a04-4df6-9acc-317da1018a7f",
    "Content-Type": "application/json"
}

for c in contacts:
    response = requests.patch(url + c, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))