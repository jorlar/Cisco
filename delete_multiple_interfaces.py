import requests
import sys

# Use self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials -> Must be changed
USER = 'developer'
PASS = 'C1sco12345'

# URL for request -> must be changed
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"


payload = {}
headers = {
    'Accept': 'application/yang-data+json'
}

#Increase or decrease number 
int_number = 5

for x in range(int_number):
    intname = "Loopback123" + str(x)
    print('Deleting ' + intname)
    url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
    response = requests.request('Delete',url, auth=(USER, PASS), headers=headers, data=payload, verify=False)
    # Print results
    print('Status Code:' + str(response.status_code))
    print('Response Text:' + response.text)

