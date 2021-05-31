from pyats.topology import loader

testbed = loader.load('lab1-testbed.yml')

testbed.devices
cisco_switches = testbed.devices['switches']

cisco_switches.connect ()

print (cisco_switches.execute('show version'))

cisco_switches.disconnect ()
