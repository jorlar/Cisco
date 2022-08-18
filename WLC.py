from netmiko import ConnectHandler

## device settings
wlc = {'host': 'x.x.x.x',
       'port': 22,
       'username': 'user',
       'password': 'psw',
       'device_type': 'cisco_wlc_ssh'}

wlc_connect = ConnectHandler(**wlc)

## CLI Commands list
wlc_show_commands = ('show time',
                     'show run-config',
                     'show run-config commands',
                     'show run-config startup-commands',
                     'show client summary',
                     'show trapflags',
                     'show traplog',
                     'show logging',
                     'show tech-support'
                     )


## Save to txt file
with open('show.txt', 'w') as f:
    for wlc_show_command in wlc_show_commands:
        f.write(wlc_connect.send_command_w_enter(wlc_show_command))

## close
f.close()
wlc_connect.disconnect()