import requests
import sys

#allow self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials
USER = 'developer'
PASS = 'C1sco12345'

# URL for GET requests
url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"

# Set yang+json as data format
headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

# Run GET
response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

print(response.text)