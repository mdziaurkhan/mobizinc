from pyats.topology import loader

testbed = loader.load('/mobizinc/pyATS/lab1-vlan_creation/lab1-testbed.yml')

testbed.devices
cisco_switches = testbed.devices['swithces']

cisco_switches.connect ()

print (cisco_switches.execute('show version'))

cisco_switches.disconnect ()
