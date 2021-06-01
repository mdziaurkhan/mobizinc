from pyats.topology import loader

testbed = loader.load('lab1_testbed_con.yaml')

testbed.devices
<<<<<<< HEAD
cisco_switches = testbed.devices['SW-192.168.1.11']
=======
cisco_switches = testbed.devices
>>>>>>> 3d96eadefe09deee0790dc8629bb39d37febaf20

cisco_switches.connect ()

print (cisco_switches.execute('show version'))
cisco_switches.disconnect ()
