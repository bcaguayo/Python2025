import requests

# Your HubSpot API key
AUTH = ""

# Get auth from /Secret/auth.py
with open('Secret/auth.txt') as f:
    AUTH = f.read().strip()

# HubSpot API URL for creating properties
url = "https://api.hubapi.com/crm/v3/properties/contacts/batch/create"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AUTH}"
}

group_name = "Call Centre Function"

# Define the properties you want to create
payload = {
    "inputs": [
        {
            "name": "calls_agent",
            "label": "Calls - Agent",
            "groupName": f"{group_name}",
            "type": "enumeration",
            "fieldType": "hubspot_user"
        },
        {
            "name": "calls_time_and_date_stamp",
            "label": "Calls - Time & Date Stamp",
            "groupName": f"{group_name}",
            "type": "bool",
            "fieldType": "booleancheckbox"
        },
        {
            "name": "calls_successful_sign_up",
            "label": "Calls - Successful Sign-up",
            "groupName": f"{group_name}",
            "type": "bool",
            "fieldType": "booleancheckbox"
        },
        {
            "name": "calls_call_back",
            "label": "Calls - Call Back",
            "groupName": f"{group_name}",
            "type": "bool",
            "fieldType": "booleancheckbox"
        },
        {
            "name": "declined",
            "label": "Calls - Declined",
            "groupName": f"{group_name}",
            "type": "bool",
            "fieldType": "booleancheckbox"
        },
        {
            "name": "calls_completed_journey",
            "label": "Calls - Completed Journey",
            "groupName": f"{group_name}",
            "type": "bool",
            "fieldType": "booleancheckbox"
        },
        {
            "name": "calls_client_retained",
            "label": "Calls - Client Retained",
            "groupName": f"{group_name}",
            "type": "bool",
            "fieldType": "booleancheckbox"
        },
        {
            "name": "calls_interaction_type",
            "label": "Calls - Interaction Type",
            "groupName": f"{group_name}",
            "type": "enumeration",
            "fieldType": "select",
            "options": [
                {"label": "Email", "value": "email"},
                {"label": "SMS", "value": "sms"},
                {"label": "Call", "value": "call"}
            ]
        },
        {
            "name": "calls_reason_for_interaction",
            "label": "Calls - Reason for Interaction",
            "groupName": f"{group_name}",
            "type": "enumeration",
            "fieldType": "select",
            "options": [
                {"label": "ID", "value": "id"},
                {"label": "Sale", "value": "sale"},
                {"label": "Query", "value": "query"}
            ]
        }
    ]
}

# Send the POST request to the HubSpot API
response = requests.post(url, headers=headers, json=payload)

# Check if the properties were created successfully
if response.status_code == 202 or response.status_code == 201 or response.status_code == 200:
    print("Property created successfully")
else:
    print(f"Error: {response.status_code} - {response.text}")
    
# Examples:
# "inputs": [
#         # Single line text
#         {
#             "name": "example_single_line_text",
#             "label": "Example Single Line Text",
#             "groupName": f"{group_name}",
#             "type": "string",
#             "fieldType": "text"
#         },

#         # Multi line text
#         {
#             "name": "example_multi_line_text",
#             "label": "Example Multi Line Text",
#             "groupName": f"{group_name}",
#             "type": "string",
#             "fieldType": "textarea"
#         },

#         # Number field
#         {
#             "name": "example_number",
#             "label": "Example Number",
#             "groupName": f"{group_name}",
#             "type": "number",
#             "fieldType": "number"
#         },

#         # Dropdown (Select)
#         {
#             "name": "example_dropdown",
#             "label": "Example Dropdown",
#             "groupName": f"{group_name}",
#             "type": "enumeration",
#             "fieldType": "select",
#             "options": [
#                 {"label": "Option 1", "value": "option1"},
#                 {"label": "Option 2", "value": "option2"}
#             ]
#         },

#         # Radio Select
#         {
#             "name": "example_radio",
#             "label": "Example Radio Select",
#             "groupName": f"{group_name}",
#             "type": "enumeration",
#             "fieldType": "radio",
#             "options": [
#                 {"label": "Choice A", "value": "a"},
#                 {"label": "Choice B", "value": "b"}
#             ]
#         },

#         # Checkbox (multiple select)
#         {
#             "name": "example_checkbox_group",
#             "label": "Example Checkbox Group",
#             "groupName": f"{group_name}",
#             "type": "enumeration",
#             "fieldType": "checkbox",
#             "options": [
#                 {"label": "Red", "value": "red"},
#                 {"label": "Blue", "value": "blue"},
#                 {"label": "Green", "value": "green"}
#             ]
#         },

#         # Boolean checkbox
#         {
#             "name": "example_boolean",
#             "label": "Example Boolean",
#             "groupName": f"{group_name}",
#             "type": "bool",
#             "fieldType": "booleancheckbox"
#         },

#         # Date picker
#         {
#             "name": "example_date",
#             "label": "Example Date",
#             "groupName": f"{group_name}",
#             "type": "date",
#             "fieldType": "date"
#         },

#         # Date & Time picker
#         {
#             "name": "example_datetime",
#             "label": "Example Date/Time",
#             "groupName": f"{group_name}",
#             "type": "datetime",
#             "fieldType": "datetime"
#         },

#         # HubSpot user field
#         {
#             "name": "example_hs_user",
#             "label": "Example HubSpot User",
#             "groupName": f"{group_name}",
#             "type": "enumeration",
#             "fieldType": "hubspot_user"
#         },

#         # Calculation property
#         {
#             "name": "example_calculation",
#             "label": "Example Calculation",
#             "groupName": f"{group_name}",
#             "type": "number",
#             "fieldType": "calculation_equation",
#             "calculationFormula": "example_number * 2"
#         },

#         # URL field
#         {
#             "name": "example_url",
#             "label": "Example URL",
#             "groupName": f"{group_name}",
#             "type": "string",
#             "fieldType": "url"
#         },

#         # Phone field
#         {
#             "name": "example_phone",
#             "label": "Example Phone Number",
#             "groupName": f"{group_name}",
#             "type": "string",
#             "fieldType": "phone"
#         }
#     ]