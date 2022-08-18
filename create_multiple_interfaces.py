import requests


# Use self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials -> Must be changed
USER = 'developer'
PASS = 'C1sco12345'

# URL for request -> must be changed
url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}


# Increase or decrease number
int_number = 50

for x in range(int_number):
    ipaddr= '3.3.3.' + str(x)
    print('Creating Loopback : ' + ipaddr)
    
    payload = '\
    {\
    "ietf-interfaces:interface": {\
    "name": "Loopback333' + str(x) + '",\
    "description": "Added with RESTCONF",\
    "type": "iana-if-type:softwareLoopback",\
    "enabled": true,\
    "ietf-ip:ipv4": {\
    "address": [\
            {\
            "ip": "3.3.3.' + str(x) + '",\
            "netmask": "255.255.255.255"\
            }\
        ]\
        }\
    }\
    }'


# Actual post request
response = requests.request('POST',url, auth=(USER, PASS), data=payload, headers=headers, verify=False)

# Print results
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)