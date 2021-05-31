from pyats.topology import loader

testbed = loader.load('lab1_testbed_con.yaml')

testbed.devices
cisco_switches = testbed.devices
for switch in cisco_switches:
    switch.connect()
    print (switch.execute('show interface status'))
    switch.disconnect()
