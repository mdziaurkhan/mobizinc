#   connectivity_check.py

from pyats import aetest
from pyats.topology import loader
from genie.libs.conf.vlan import vlan
logger = logging.getLogger(__name__)
import logging

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def establish_connections(self, steps):
        testbed = loader.load('lab3_testbed.yaml')
        testbed.devices
        for i in testbed.devices:
            with steps.start('Connecting to %s' % i):
                testbed.devices[i].connect()

class VlanCreation(aetest.Testcase):
    @aetest.setup
    def Create_Vlan(self, steps, vlan):
        testbed = loader.load('lab3_testbed.yaml')
        testbed.devices
        for i in testbed.devices:
            with steps.start('Configuring VLAN into %s' % i):
                #new_vlan = Vlan(vlan_id = "20", name = "ziatest")
                #testbed.devices[i].add_feature(new_vlan)
                #new_vlan.build_config(apply = True)
                logger.info('Vlan = %s' % vlan)

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
    import sys

    testbed = loader.load('lab3_testbed.yaml')
    testbed.devices

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',type = loader.load)
    parser.add_argument('--vlan', dest = 'vlan')
    args, unknown = parser.parse_known_args()

    vlan = int(args.vlan)

    aetest.main(**vars(args))
