#====[LOC Preparation on HubSpot Workflow]=======================================================================================================
# ABSTRACT: This script prepares the Letter of Complaint (LOC) for HubSpot workflows, handling file extraction, API calls, and error management.
# DATE: 2023-10-01
# VERSION: 1.0
# DESCRIPTION:   This script is designed to be used in a HubSpot workflow to prepare the Letter of Complaint (LOC) by extracting file properties, 
#                handling various formats, and making API calls to retrieve necessary data. It includes robust error handling and logging for 
#                debugging purposes.  Use it in conjunction with HubSpot workflow: CCL Presubmission Preparation: 
#                https://app-eu1.hubspot.com/workflows/145626201/platform/flow/2370956536/edit
#                The workflow is triggered by: deal.ready_for_pre_submission_processing.
#================================================================================================================================================
import requests
import json
import os
import re
from datetime import datetime, timezone
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def format_date(timestamp):
    """Format date from various input formats"""
    if not timestamp:
        return 'Date not available'
    try:
        if isinstance(timestamp, str) and '-' in timestamp:
            date_obj = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        else:
            date_obj = datetime.fromtimestamp(int(timestamp) / 1000, tz=timezone.utc)
        return date_obj.strftime('%d/%m/%Y')
    except (ValueError, TypeError) as e:
        logger.warning(f"Date formatting error: {e}")
        return 'Invalid date'

def safe_string(value):
    """Safely convert value to string"""
    return str(value).strip() if value and str(value).strip() else ''

def get_signed_file_url(file_id, access_token):
    """Get signed URL for a HubSpot file"""
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        response = requests.get(
            f"https://api.hubapi.com/files/v3/files/{file_id}/signed-url",
            headers=headers,
            timeout=5
        )
        
        if response.status_code == 200:
            signed_url_data = response.json()
            signed_url = signed_url_data.get('url')
            if signed_url:
                logger.info(f"✅ Got signed URL for file {file_id}")
                return signed_url
        
        logger.error(f"Failed to get signed URL for file {file_id}: HTTP {response.status_code}")
        return None
        
    except Exception as e:
        logger.error(f"Error getting signed URL for file {file_id}: {e}")
        return None

def main(event):
    """
    Complete workflow with proper environment configuration
    """
    try:
        logger.info("🚀 Complete Workflow started")
        
        # Get deal ID
        deal_id = event.get('object', {}).get('objectId')
        if not deal_id:
            raise ValueError('No deal ID available')
        
        logger.info(f"📋 Processing deal: {deal_id}")
        
        # Get available input fields
        input_fields = event.get('inputFields', {})
        logger.info(f"📥 Available input fields: {list(input_fields.keys())}")
        
        # Get contact ID
        contact_id = input_fields.get('hs_object_id')
        if contact_id:
            logger.info(f"👤 Contact ID from hs_object_id: {contact_id}")
        
        # Extract core fields
        finance_agreement_number = safe_string(input_fields.get('finance_agreement_number', ''))
        firstname = safe_string(input_fields.get('first_name_cfc', ''))
        lastname = safe_string(input_fields.get('last_name_cfc', ''))
        agreement_start_date = safe_string(input_fields.get('agreement_start_date', ''))
        premium_amount = input_fields.get('premium_amount')
        
        logger.info(f"👤 Core data: {firstname} {lastname}, Agreement: {finance_agreement_number}")
        
        # Validate core required fields
        if not firstname or not lastname or not finance_agreement_number:
            raise ValueError(f"Missing core fields: firstname={firstname}, lastname={lastname}, agreement={finance_agreement_number}")
        
        # Get environment setup - FIXED with proper detection
        access_token = os.environ.get('HS_PRIVATE_APP_PROCESSING')
        if not access_token:
            raise ValueError("HS_PRIVATE_APP_PROCESSING access token is required")
        
        # Environment detection with debugging
        raw_environment = os.environ.get('ENVIRONMENT', 'dev')
        
        environment = raw_environment.lower()
        logger.info(f"🌍 Raw environment: '{raw_environment}' -> Processed: '{environment}'")
        
        # DEBUG: Show which branch we're taking
        if environment == 'Prod':
            logger.info("🔧 Using PRODUCTION configuration")
            aws_api_key = os.environ.get('PROD_AWS_ACCESS_KEY')
            api_endpoint = os.environ.get('PROD_AWS_API_URL')
        else:
            logger.info("🔧 Using DEVELOPMENT configuration")
            aws_api_key = os.environ.get('DEV_AWS_ACCESS_KEY')
            api_endpoint = os.environ.get('DEV_AWS_API_URL')
        
        # Log what we found
        logger.warning(f"🔑 AWS API Key found: {bool(aws_api_key)}")
        logger.warning(f"🌐 API Endpoint: {api_endpoint}")
        
        # Validate required environment variables
        if not aws_api_key:
            raise ValueError(f"Missing AWS API key for {environment} environment")
        
        if not api_endpoint:
            raise ValueError(f"Missing API endpoint for {environment} environment")
        
        # Ensure endpoint format is correct for API Gateway with stage
        if not api_endpoint.endswith('/'):
            api_endpoint += '/'
        
        # Add stage to the endpoint if not already present
        if environment == 'Prod':
            if '/Prod/' not in api_endpoint and not api_endpoint.endswith('Prod/'):
                api_endpoint += 'Prod/'
                logger.info("🔧 Added 'Prod/' stage to endpoint")
        else:
            if '/dev/' not in api_endpoint and not api_endpoint.endswith('dev/'):
                api_endpoint += 'dev/'
                logger.info("🔧 Added 'dev/' stage to endpoint")
        
        # Add the generate-doc path to the endpoint
        full_api_url = f"{api_endpoint.rstrip('/')}/generate-doc"
        
        portal_id = os.environ.get('HS_PORTAL_ID', '145626201')
        
        logger.warning(f"🎯 Final API URL: {full_api_url}")
        logger.warning(f"🏢 Portal ID: {portal_id}")
        
        # Get missing data via API
        logger.info("🔍 Fetching missing data via API...")
        
        try:
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            # Get deal with associations
            deal_url = f"https://api.hubapi.com/crm/v3/objects/deals/{deal_id}"
            deal_params = {
                'properties': 'duration,client_reference,deal_address',
                'associations': 'contacts,2-136419057'
            }
            
            deal_response = requests.get(deal_url, headers=headers, params=deal_params, timeout=5)
            deal_response.raise_for_status()
            deal_data = deal_response.json()
            
            # Extract deal data
            deal_props = deal_data.get('properties', {})
            duration = safe_string(deal_props.get('duration', ''))
            client_reference = safe_string(deal_props.get('client_reference', ''))
            deal_address = safe_string(deal_props.get('deal_address', ''))
            
            associations = deal_data.get('associations', {})
            
            # Get contact ID if we don't have it
            if not contact_id and 'contacts' in associations and associations['contacts']['results']:
                contact_id = associations['contacts']['results'][0]['id']
                logger.info(f"👤 Contact ID from associations: {contact_id}")
            
            # Get lender ID
            lender_id = None
            if '2-136419057' in associations and associations['2-136419057']['results']:
                lender_id = associations['2-136419057']['results'][0]['id']
                logger.info(f"🏦 Lender ID: {lender_id}")
            
            # Get contact data
            birth_date = 'Date not available'
            client_previous_last_name = ''
            client_previous_address = ''
            contact_address = ''
            loa_lender_document = ''
            
            if contact_id:
                contact_url = f"https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}"
                contact_params = {
                    'properties': 'birth_date,date_of_birth,client_previous_last_name,client_previous_address,address,loa_lender_document'
                }
                
                contact_response = requests.get(contact_url, headers=headers, params=contact_params, timeout=5)
                if contact_response.status_code == 200:
                    contact_data = contact_response.json()
                    contact_props = contact_data.get('properties', {})
                    
                    # Try both birth_date and date_of_birth
                    birth_date_raw = contact_props.get('birth_date') or contact_props.get('date_of_birth')
                    if birth_date_raw:
                        birth_date = birth_date_raw
                    
                    client_previous_last_name = safe_string(contact_props.get('client_previous_last_name', ''))
                    client_previous_address = safe_string(contact_props.get('client_previous_address', ''))
                    contact_address = safe_string(contact_props.get('address', ''))
                    loa_lender_document = safe_string(contact_props.get('loa_lender_document', ''))
                    
                    logger.info(f"✅ Contact data: birth_date={birth_date}, loa_doc={loa_lender_document}")
            
            # Get lender data
            lender_name = 'Lender not found'
            lender_full_address = 'Lender not found'
            
            if lender_id:
                lender_url = f"https://api.hubapi.com/crm/v3/objects/2-136419057/{lender_id}"
                lender_params = {
                    'properties': 'lender_name,lender_address,lender_email'
                }
                
                lender_response = requests.get(lender_url, headers=headers, params=lender_params, timeout=5)
                if lender_response.status_code == 200:
                    lender_data = lender_response.json()
                    lender_props = lender_data.get('properties', {})
                    
                    lender_name = lender_props.get('lender_name', f'Lender {lender_id}')
                    lender_addr = lender_props.get('lender_address', '')
                    lender_email = lender_props.get('lender_email', '')
                    
                    # Format full address
                    if lender_addr and lender_email and lender_addr != lender_email:
                        lender_full_address = f"{lender_name}\n{lender_addr}\nEmail: {lender_email}"
                    elif lender_addr:
                        lender_full_address = f"{lender_name}\n{lender_addr}"
                    elif lender_email:
                        lender_full_address = f"{lender_name}\nEmail: {lender_email}"
                    else:
                        lender_full_address = lender_name
                    
                    logger.info(f"✅ Lender data: {lender_name}")
            
        except Exception as e:
            logger.warning(f"⚠️ API fetch failed: {e}")
            # Use defaults
            duration = ''
            client_reference = deal_id
            deal_address = ''
            birth_date = 'Date not available'
            client_previous_last_name = ''
            client_previous_address = ''
            contact_address = ''
            loa_lender_document = ''
            lender_name = 'Lender lookup failed'
            lender_full_address = 'Lender lookup failed'
        
        # Format dates
        formatted_birth_date = format_date(birth_date)
        formatted_agreement_start_date = format_date(agreement_start_date)
        
        # Build payment terms
        full_payment_terms = 'Payment terms to be confirmed from credit report'
        if premium_amount and duration:
            full_payment_terms = f"£{premium_amount} x {duration} months"
        elif premium_amount:
            full_payment_terms = f"£{premium_amount} (duration pending)"
        
        # Address fallback
        address = deal_address or contact_address or 'Address not available'
        
        # Other fields with fallbacks
        full_previous_address = client_previous_address or 'No previous address on file'
        best_client_reference = client_reference or deal_id
        
        # File naming
        uk_timestamp = datetime.now().strftime('%Y%m%d')
        footer_file_name = f"{firstname}_{lastname}_{finance_agreement_number}_{uk_timestamp}"
        
        # Build CRM data
        crm_data = {
            'firstname': firstname,
            'lastname': lastname,
            'birth_date': formatted_birth_date,
            'address': address,
            'client_previous_last_name': client_previous_last_name,
            'full_previous_address': full_previous_address,
            'client_reference': best_client_reference,
            'client_reference_deal_id': best_client_reference,
            'finance_agreement_number': finance_agreement_number,
            'agreement_start_date': formatted_agreement_start_date,
            'duration': str(duration) if duration else '',
            'lender': lender_name,
            'lender_full_address': lender_full_address,
            'full_payment_terms': full_payment_terms,
            'footer_file_name': footer_file_name,
            'deal_id': deal_id,
            'loa_document_reference': loa_lender_document
        }
        
        logger.info("✅ CRM data compiled")
        
        # Get file URLs
        logger.info("📁 Getting file URLs...")
        
        # LOC Template - fixed URL
        loc_template_url = "https://145626201.fs1.hubspotusercontent-eu1.net/hubfs/145626201/Templates/Letter%20of%20Complaint/LOC%20Standard%20Merge%20Template.pdf"
        
        # LOA Document - get signed URL if we have the file ID
        loa_signed_url = ''
        if loa_lender_document:
            if loa_lender_document.isdigit():
                loa_signed_url = get_signed_file_url(loa_lender_document, access_token)
                if loa_signed_url:
                    logger.info(f"📎 LOA signed URL obtained for file {loa_lender_document}")
                else:
                    logger.warning(f"⚠️ Failed to get signed URL for LOA file {loa_lender_document}")
            else:
                loa_signed_url = loa_lender_document
                logger.info(f"📎 LOA URL used directly")
        
        if not loa_signed_url:
            logger.warning("⚠️ No LOA document URL available")
            loa_signed_url = ''
        
        # Prepare AWS Lambda payload
        lambda_payload = {
            'action': 'generate_loc',
            'crmData': crm_data,
            'source': 'CCL - LOC Generation Python (Fixed Environment)',
            'signed_file_urls': {
                "loc_template_url": loc_template_url,
                "loa_document_url": loa_signed_url,
                "footer_file_name": footer_file_name
            },
            'hubspot_auth': {
                "token": access_token,
                "portal_id": portal_id
            }
        }

        lambda_headers = {
            'Content-Type': 'application/json',
            'X-HubSpot-Portal': portal_id,
            'X-Workflow-Version': 'python-fixed-env-1.0',
            'X-Environment': environment,
            'X-AWS-Stage': environment,
            'x-api-key': aws_api_key
        }
        
        logger.info("☁️ Calling AWS Lambda...")
        logger.info(f"🎯 URL: {full_api_url}")
        logger.info(f"📁 Template URL: {loc_template_url}")
        logger.info(f"📎 LOA URL: {loa_signed_url}")
        logger.info(f"🔑 API Key length: {len(aws_api_key) if aws_api_key else 0}")
        
        # Call AWS Lambda with detailed error handling
        processing_start_time = datetime.now()
        
        try:
            lambda_response = requests.post(
                full_api_url,
                headers=lambda_headers,
                json=lambda_payload,
                timeout=30
            )
            
            processing_time = (datetime.now() - processing_start_time).total_seconds() * 1000
            
            logger.info(f"📨 AWS Response: {lambda_response.status_code}")
            logger.info(f"📨 AWS Response Headers: {dict(lambda_response.headers)}")
            
            # Log response content for debugging
            response_text = lambda_response.text
            logger.info(f"📨 AWS Response Text (first 500 chars): {response_text[:500]}")
            
            if lambda_response.status_code == 200:
                try:
                    lambda_data = lambda_response.json()
                    lambda_body = lambda_data.get('body', lambda_data)
                    
                    if isinstance(lambda_body, str):
                        try:
                            lambda_body = json.loads(lambda_body)
                        except json.JSONDecodeError:
                            lambda_body = lambda_data
                    
                    file_url = lambda_body.get('fileUrl', '') or lambda_body.get('directFileUrl', '')
                    file_id = lambda_body.get('fileId', '')
                    file_name = lambda_body.get('filename', '') or footer_file_name + '.pdf'
                    
                    logger.info(f"✅ LOC generation successful! File: {file_name}")
                    logger.info(f"📁 File URL: {file_url}")
                    logger.info(f"🆔 File ID: {file_id}")
                    
                    timestamp = datetime.now(timezone.utc).isoformat()
                    date_formatted = datetime.now().strftime('%d/%m/%Y')
                    
                    return {
                        'outputFields': {
                            'status': f'✅ LOC processed successfully (fixed environment)',
                            'processing_complete': True,
                            'advance_stage': True,
                            'loc_file_id': file_id,
                            'loc_filename': file_name,
                            'loc_file_url': file_url,
                            'loc_document': file_id,
                            'loc_document_url': file_url,
                            'loc_generation_date': date_formatted,
                            'loc_drafted': 'Yes',
                            'loc_generation_status': 'Success',
                            'tokens_replaced_count': lambda_body.get('tokensReplaced', 0),
                            'document_pages': lambda_body.get('documentPages', 0),
                            'loa_pages_added': lambda_body.get('loaPagesAdded', 0),
                            'processing_time_ms': int(processing_time),
                            'workflow_version': 'python-fixed-env-1.0',
                            'aws_environment': environment,
                            'loa_document_found': bool(loa_signed_url)
                        }
                    }
                except json.JSONDecodeError as e:
                    logger.error(f"❌ Failed to parse AWS JSON response: {e}")
                    logger.error(f"Raw response: {response_text}")
                    raise ValueError(f"Invalid JSON response from AWS: {e}")
            else:
                # Non-200 response
                error_message = f'HTTP {lambda_response.status_code}'
                try:
                    error_body = lambda_response.json()
                    error_message = error_body.get('message', error_message)
                    logger.error(f"AWS Error Response: {error_body}")
                except:
                    logger.error(f"AWS Error Response Text: {response_text}")
                    
                logger.error(f"❌ AWS processing failed: {error_message}")
                
                timestamp = datetime.now(timezone.utc).isoformat()
                date_formatted = datetime.now().strftime('%d/%m/%Y')
                
                return {
                    'outputFields': {
                        'status': f'❌ AWS processing failed: {error_message}',
                        'processing_complete': False,
                        'error_message': error_message,
                        'loc_generation_date': date_formatted,
                        'loc_drafted': 'No',
                        'loc_generation_status': 'Failed',
                        'workflow_version': 'python-fixed-env-1.0',
                        'aws_response_code': lambda_response.status_code,
                        'aws_url_used': full_api_url,
                        'aws_environment': environment
                    }
                }
                
        except requests.exceptions.Timeout:
            logger.error("❌ AWS Lambda call timed out after 30 seconds")
            timestamp = datetime.now(timezone.utc).isoformat()
            date_formatted = datetime.now().strftime('%d/%m/%Y')
            
            return {
                'outputFields': {
                    'status': '❌ AWS Lambda call timed out',
                    'processing_complete': False,
                    'error_message': 'AWS Lambda call timed out after 30 seconds',
                    'loc_generation_date': date_formatted,
                    'loc_drafted': 'No',
                    'loc_generation_status': 'Failed',
                    'workflow_version': 'python-fixed-env-1.0',
                    'aws_url_used': full_api_url
                }
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ AWS Lambda request failed: {e}")
            timestamp = datetime.now(timezone.utc).isoformat()
            date_formatted = datetime.now().strftime('%d/%m/%Y')
            
            return {
                'outputFields': {
                    'status': f'❌ AWS Lambda request failed: {str(e)}',
                    'processing_complete': False,
                    'error_message': str(e),
                    'loc_generation_date': date_formatted,
                    'loc_drafted': 'No',
                    'loc_generation_status': 'Failed',
                    'workflow_version': 'python-fixed-env-1.0',
                    'aws_url_used': full_api_url
                }
            }
        
    except Exception as error:
        logger.error(f"❌ Workflow Error: {error}")
        
        return {
            'outputFields': {
                'status': f'❌ Workflow failed: {str(error)}',
                'processing_complete': False,
                'error_message': str(error),
                'loc_generation_date': datetime.now().strftime('%d/%m/%Y'),
                'loc_drafted': 'No',
                'loc_generation_status': 'Failed',
                'workflow_version': 'python-fixed-env-1.0'
            }
        }


# Alternative entry points
def handler(event):
    return main(event)

def lambda_handler(event, context=None):
    return main(event)

def hubspot_handler(event):
    return main(event)