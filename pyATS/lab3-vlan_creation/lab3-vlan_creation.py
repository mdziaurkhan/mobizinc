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
                testbed.devices[i].add_feature(new_vlan)
                new_vlan.build_config(apply = True)


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self, steps):
        for i in testbed.devices:
            with steps.start('Disconnecting from %s' % i):
                testbed.devices[i].disconnect()



if __name__ == '__main__':
    import argparse
    from pyats.topology import loader
    from genie.libs.conf.vlan import vlan

    testbed = loader.load('lab3_testbed.yaml')
    testbed.devices
    new_vlan = 20

    aetest.main()
