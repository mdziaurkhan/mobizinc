from pyats.topology import loader

testbed = loader.load('lab1_testbed_con.yaml')

testbed.devices
cisco_switches = testbed.devices['NexSW-192.168.1.12']

cisco_switches.connect ()

print (cisco_switches.execute('show version'))
cisco_switches.disconnect ()
