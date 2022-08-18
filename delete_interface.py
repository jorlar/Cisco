from urllib import response
from wsgiref import headers
import requests

# Use self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials -> Must be changed
USER = 'developer'
PASS = 'C1sco12345'

#Change intname
intname = "Loopback6666"


# URL for request -> must be changed
url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=" + intname

# JSON Payload 
payload = {}

# Headers to send 
headers = {
    'Accept': 'application/yang-data+json'
}

# Actual post request
response = requests.request('DELETE',url, auth=(USER, PASS), headers=headers, data=payload, verify=False)

# Print results
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)