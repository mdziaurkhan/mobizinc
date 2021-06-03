#   connectivity_check.py

from pyats import aetest

class CommonSetup(aetest.CommonSetup):
    for i in testbed.devices:
        @aetest.subsection
        def establish_connections(self, steps, i):
            with steps.start('Connecting to %s' % i):
                i.connect()


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, i):
        with steps.start('Disconnecting from %s' % i):
            i.disconnect()


if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    testbed = loader.load('lab2_testbed.yaml')

    testbed.devices

    #for i in testbed.devices:
    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',type = loader.load)
    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
