import requests

# Set the API endpoint
url = "https://api.hubapi.com/crm/v3/objects/contacts"

# Set the request headers
headers = {
   "Content-Type": "application/json",
   "Authorization": "Bearer pat-eu1-c8242757-5a04-4df6-9acc-317da1018a7f"
}

# Set the contact information
contact = {
   "properties": {
       "email": "test@ccl.com",
       "firstname": "Test",
       "lastname": "Test"
   }
}

# Send the request
response = requests.post(url, json=contact, headers=headers)

if response.status_code == 201:
   print("Contact Created Successfully")
else:
   print("Failed To Create Contact")