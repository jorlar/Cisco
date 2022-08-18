from urllib import response
from wsgiref import headers
import requests

# Use self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials -> Must be changed
USER = 'developer'
PASS = 'C1sco12345'

# URL for request -> must be changed
url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"


# JSON Payload - using \ to continue the line in python
payload = '\
    {\
        "ietf-interfaces:interface": {\
            "name": "Loopback6667", \
            "description": "Added with RESTCONF", \
            "type": "iana-if-type:softwareLoopback", \
            "enabled": true, \
            "ietf-ip:ipv4": {\
                "address": [\
                    {\
                        "ip": "6.6.6.7", \
                        "netmask": "255.255.255.255"\
                    }\
                ] \
            }\
        }\
    }'

# Headers to send 
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}

# Actual post request
response = requests.request('POST',url, auth=(USER, PASS), headers=headers, data=payload, verify=False)

# Print results
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)