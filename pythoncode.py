import requests
import os

# Zapier passes the id_data as an environment variable or input_data argument
id_data = input_data.get("id_data")  # Gets 'id_data' from Zapier input

# Airtable API settings
api_key = "YOUR_API_KEY"
base_id = "YOUR_BASE_ID"
table_id = "YOUR_TABLE_ID"
url = f"https://api.airtable.com/v0/{base_id}/{table_id}/{id_data}"

# API headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Data to update the status
data = {
    "fields": {
        "Status": "Published"
    }
}

# PATCH request
response = requests.patch(url, headers=headers, json=data)

# Result
if response.status_code == 200:
    output = {'success': "Status updated to 'Published'", 'record': response.json()}
else:
    output = {'error': f"Error updating the record: {response.status_code}"}

print(output)
