import requests

AUTH = ""
# Get auth from /Secret/auth.py
with open('/Secret/auth.py') as f:
    AUTH = f.read().strip()

# Set the API endpoint
url = "https://api.hubapi.com/crm/v3/objects/contacts"

# Set the request headers
headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {AUTH}"
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