from netmiko import ConnectHandler

nx_os = {
    'device_type': 'cisco_ios',
    # Change ip usr and psw
    'ip': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22 
}

net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief')
print(output)