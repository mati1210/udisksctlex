# SPDX-License-Identifier: MPL-2.0
# doc: https://storaged.org/doc/udisks2-api/latest/gdbus-org.freedesktop.UDisks2.Manager.html
import sdbus
from . import SERVICE_NAME, Options


class Manager(
    sdbus.DbusInterfaceCommon, interface_name="org.freedesktop.UDisks2.Manager"
):

    def __init__(self, bus: sdbus.SdBus | None = None):
        super().__init__(SERVICE_NAME, "/org/freedesktop/UDisks2/Manager", bus)

    @sdbus.dbus_method("ha{sv}", "o")
    def loop_setup(self, fd: int, options: Options) -> str:
        raise NotImplementedError
