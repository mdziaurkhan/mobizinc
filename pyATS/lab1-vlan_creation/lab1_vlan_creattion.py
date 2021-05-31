from pyats.topology import loader

testbed = loader.load('lab1_testbed_con.yaml')

testbed.devices
cisco_switches = testbed.devices
for switch in cisco_switches:
    cisco_switches.connect()
    print (cisco_switches.execute('show interface status'))
    cisco_switches.disconnect()
