#   connectivity_check.py

from pyats import aetest
from pyats.topology import loader
from genie.libs.conf.vlan import vlan

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def establish_connections(self, steps):
        testbed = loader.load('lab3_testbed.yaml')
        testbed.devices
        for i in testbed.devices:
            with steps.start('Connecting to %s' % i):
                testbed.devices[i].connect()

class VlanCreation(aetest.Testcase):
    @aetest.subsection
    def Create_Vlan(self, steps):
        testbed = loader.load('lab3_testbed.yaml')
        testbed.devices
        for i in testbed.devices:
            with steps.start('Configuring VLAN into %s' % i):
                new_vlan = Vlan(vlan_id = "20", name = "ziatest")
                device.add_feature(new_vlan)
                new_vlan.build_config(apply = True)

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps):
        testbed = loader.load('lab3_testbed.yaml')
        testbed.devices
        for i in testbed.devices:
            with steps.start('Disconnecting from %s' % i):
                testbed.devices[i].disconnect()



if __name__ == '__main__':
    import argparse
    from pyats.topology import loader
    from genie.libs.conf.vlan import vlan

    testbed = loader.load('lab3_testbed.yaml')
    testbed.devices

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',type = loader.load)
    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
