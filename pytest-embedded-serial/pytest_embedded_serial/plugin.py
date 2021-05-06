from types import ModuleType

import pytest

from ._serial import open_port_session


def pytest_addoption(parser):
    group = parser.getgroup('embedded')
    group.addoption('--port',
                    help='serial port')


@pytest.hookimpl
def pytest_plugin_registered(plugin, manager):
    if not isinstance(plugin, ModuleType) or plugin.__name__ != 'pytest_embedded.plugin':
        return

    plugin.KNOWN_OPTIONS['DUT'].append('port')

    setattr(plugin.DUT, 'open_port_session', open_port_session)
