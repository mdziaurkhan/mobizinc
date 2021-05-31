from pyats.topology import loader

testbed = loader.load('lab1_testbed_con.yaml')

testbed.devices

for switch in cisco_switches:
    cisco_switches = testbed.devices
    switch.connect()
    print (switch.execute('show interface status'))
    switch.disconnect()
