from pyats.topology import loader

testbed = loader.load('lab1_testbed_con.yaml')

testbed.devices
<<<<<<< HEAD
cisco_switches = testbed.devices['SW-192.168.1.11']

cisco_switches.connect ()

print (cisco_switches.execute('show version'))
cisco_switches.disconnect ()
=======

for switch in cisco_switches:
    cisco_switches = testbed.devices
    switch.connect()
    print (switch.execute('show interface status'))
    switch.disconnect()
>>>>>>> 67c006deca187ec9b44cfe3c9b1b213e981ae7ce
