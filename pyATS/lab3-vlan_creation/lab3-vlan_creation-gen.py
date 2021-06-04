#   connectivity_check.py

from pyats import aetest

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def establish_connections(self, steps):
        for i in testbed.devices:
            with steps.start('Connecting to %s' % i):
                testbed.devices[i].connect()

class VlanCreation(aetest.Testcase):
    @aetest.setup
    def Create_Vlan(self, steps):
        for i in testbed.devices:
            with steps.start('Configuring VLAN into %s' % i):
                #testbed.devices[i].configure(""" vlan 20
                #name ziatest
                #""")
                testbed.devices[i].add_feature(new_vlan)
                #new_vlan.build_config()
                output = new_vlan.build_config(new_vlan)
                #testbed.devices[i].build_config(new_vlan)
                output(testbed.devices[i])


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self, steps):
        for i in testbed.devices:
            with steps.start('Disconnecting from %s' % i):
                testbed.devices[i].disconnect()



if __name__ == '__main__':
    import argparse
    from pyats.topology import loader
    from genie.libs.conf.vlan import Vlan
    from genie.conf import Genie
    genie_testbed = Genie.init(testbed=pyats_testbed)
    assert Genie.testbed == genie_testbed
    #from genie.libs.conf.interface import interface
    #import genie



    testbed = loader.load('lab3_testbed.yaml')
    testbed.devices
    new_vlan = Vlan(vlan_id = "30", name = "ziatest")
    #new_vlan.vlan_id = "20"
    #new_vlan.name = "ziatest"

    aetest.main()
