#   connectivity_check.py

from pyats import aetest

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def establish_connections(self, steps):
        for i in testbed.devices:
            with steps.start('Connecting to %s' % i):
                testbed.devices[i].connect()

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps):
        for i in testbed.devices:
            with steps.start('Disconnecting from %s' % i):
                testbed.devices[i].disconnect()



if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    testbed = loader.load('lab2_testbed.yaml')
    testbed.devices

    aetest.main()
