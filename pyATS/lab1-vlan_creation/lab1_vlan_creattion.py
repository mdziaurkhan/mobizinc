from pyats.topology import loader

testbed = loader.load('lab1_testbed_con.yaml')

testbed.devices
cisco_switches = testbed.devices[0]

cisco_switches.connect ()

print (cisco_switches.execute('show version'))
cisco_switches.disconnect ()
