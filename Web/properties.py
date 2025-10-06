import requests
import json

# Your HubSpot API key
access_token = 'pat-eu1-c8242757-5a04-4df6-9acc-317da1018a7f'

# HubSpot API URL for creating properties
url = "https://api.hubapi.com/crm/v3/properties/contacts/batch/create"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

group_name = "aml_automated"

# Define the properties you want to create
payload = {
    "inputs": [
        # {
        #     "name": "ln_idu_decision",
        #     "label": "LexusNexus IDU Decision",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #         {"label": "Pass", "value": "pass"},
        #         {"label": "Refer", "value": "refer"},
        #         {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_idu_scorecard",
        #     "label": "LexusNexus IDU Scorecard",
        #     "groupName": f"{group_name}",
        #     "type": "string",
        #     "fieldType": "text"
        # },
        # {
        #     "name": "ln_idu_score",
        #     "label": "LexusNexus IDU Score",
        #     "groupName": f"{group_name}",
        #     "type": "number",
        #     "fieldType": "number"
        # },
        # {
        #     "name": "ln_idu_checked_at",
        #     "label": "LexusNexus IDU Timestamp",
        #     "groupName": f"{group_name}",
        #     "type": "datetime",
        #     "fieldType": "date"
        # },
        # {
        #     "name": "ln_idu_transaction_id",
        #     "label": "LexusNexus IDU Transaction ID",
        #     "groupName": f"{group_name}",
        #     "type": "string",
        #     "fieldType": "text"
        # },
        # {
        #     "name": "ln_check_electoral_roll",
        #     "label": "LexusNexus Check Electoral Roll",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #         {"label": "No Match", "value": "no_match"},
        #         {"label": "Match", "value": "match"},
        #         {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_tracesmart",
        #     "label": "LexusNexus Check Tracesmart",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #         {"label": "No Match", "value": "no_match"},
        #         {"label": "Match", "value": "match"},
        #         {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_telephone_directory",
        #     "label": "LexusNexus Check Telephone Directory",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #         {"label": "No Match", "value": "no_match"},
        #         {"label": "Match", "value": "match"},
        #         {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_credit_active",
        #     "label": "LexusNexus Check Credit Active",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_dob_verification",
        #     "label": "LexusNexus Check DOB Verification",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_age_verification",
        #     "label": "LexusNexus Check Age Verification",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_pep_sanction",
        #     "label": "LexusNexus Check PEP Sanction",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_mortality",
        #     "label": "LexusNexus Check Mortality",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_gone_away",
        #     "label": "LexusNexus Check Gone Away",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_ccj",
        #     "label": "LexusNexus Check CCJ",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_insolvency",
        #     "label": "LexusNexus Check Insolvency",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # },
        # {
        #     "name": "ln_check_company_director",
        #     "label": "LexusNexus Check Company Director",
        #     "groupName": f"{group_name}",
        #     "type": "enumeration",
        #     "fieldType": "select",
        #     "options": [
        #     {"label": "No Match", "value": "no_match"},
        #     {"label": "Match", "value": "match"},
        #     {"label": "Fail", "value": "fail"}
        #     ]
        # }  
        {
            "name": "ln_detail_insolvency",
            "label": "LexusNexus IDU Insolvency Details",
            "groupName": f"{group_name}",
            "type": "string",
            "fieldType": "text"
        },
        {
            "name": "ln_detail_pep_sanction",
            "label": "LexusNexus IDU PEP Sanction Details",
            "groupName": f"{group_name}",
            "type": "string",
            "fieldType": "text"
        },
        {
            "name": "ln_detail_mortality",
            "label": "LexusNexus IDU Mortality Details",
            "groupName": f"{group_name}",
            "type": "string",
            "fieldType": "text"
        },
        {
            "name": "ln_detail_ccj",
            "label": "LexusNexus IDU CCJ Details",
            "groupName": f"{group_name}",
            "type": "string",
            "fieldType": "text"
        },
        {
            "name": "ln_idu_raw_json",
            "label": "LexusNexus IDU JSON Response",
            "groupName": f"{group_name}",
            "type": "string",
            "fieldType": "textarea"
        }
    ]
}

# Example Property model (HubSpot):
# •	ln_idu_decision — Dropdown: Pass, Refer, Fail
# •	ln_idu_scorecard — Single-line text
# •	ln_idu_score — Number (or text if needed)
# •	ln_idu_checked_at — Datetime
# •	ln_idu_transaction_id — Single-line text
# •	Per-check fields (each a Dropdown with options No Match, Match, Fail):
#     o	ln_check_electoral_roll
#     o	ln_check_tracesmart
#     o	ln_check_telephone_directory
#     o	ln_check_credit_active
#     o	ln_check_dob_verification
#     o	ln_check_age_verification
#     o	ln_check_pep_sanction
#     o	ln_check_mortality
#     o	ln_check_gone_away
#     o	ln_check_ccj
#     o	ln_check_insolvency
#     o	ln_check_company_director
# (if possible) text fields for detail strings:
# o	ln_detail_insolvency, ln_detail_pep_sanction, ln_detail_mortality, ln_detail_ccj, etc.
# (if possible) ln_idu_raw_json — Long text

# Send the POST request to the HubSpot API
response = requests.post(url, headers=headers, json=payload)

# Check if the properties were created successfully
if response.status_code == 202 or response.status_code == 201 or response.status_code == 200:
    print("Property created successfully")
else:
    print(f"Error: {response.status_code} - {response.text}")
