import requests     #type: ignore
import json

contacts = {"321820069051", "321820069050", "321820068089", 
            "321820068088", "321820068087", "321820068086"}

url = "https://api.hubapi.com/crm/v3/objects/deals/"

payload = { "properties": {
        "lost_reason": "Duplicate Case",
        "dealstage": "1234144467"
    } }

headers = {
    "Authorization": "Bearer pat-eu1-c8242757-5a04-4df6-9acc-317da1018a7f",
    "Content-Type": "application/json"
}

for c in contacts:
    response = requests.patch(url + c, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))