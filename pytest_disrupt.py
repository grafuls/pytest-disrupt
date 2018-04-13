# -*- coding: utf-8 -*-
from __future__ import print_function


class DisruptHook(object):
    def __init__(self, config):
        self.config = config

    def pytest_runtest_setup(self, item):
        if "disrupt" not in item.keywords:
            return
        # TODO: timing?
        dsrmarker = item.get_marker("disrupt")
        if dsrmarker:
            # TODO: predefined actions?
            dsraction = dsrmarker.args[0]
            dsrhost = dsrmarker.args[1]
            if dsraction:
                if dsraction.upper() == "REBOOT":
                    # TODO: print to stdout during execution
                    print(
                        "Restarting host: %s" %
                        dsrhost
                    )
                    # TODO: figure out credentials (HOST object?)


def pytest_configure(config):
    config.addinivalue_line(
        'markers',
        "disrupt(action, host): mark test to run with a "
        "disruptive action"
    )

    disrupt = DisruptHook(config)
    assert config.pluginmanager.register(disrupt, "disrupt_helper")
