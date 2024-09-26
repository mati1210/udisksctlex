# SPDX-License-Identifier: MPL-2.0
# doc: https://storaged.org/doc/udisks2-api/latest/gdbus-org.freedesktop.UDisks2.Filesystem.html
import sdbus
from . import SERVICE_NAME, Options


class Filesystem(
    sdbus.DbusInterfaceCommon, interface_name="org.freedesktop.UDisks2.Filesystem"
):
    def __init__(self, object_path: str, bus: sdbus.SdBus | None = None):
        super().__init__(SERVICE_NAME, object_path, bus)

    @sdbus.dbus_property("t")
    def size(self) -> int:
        raise NotImplementedError

    @sdbus.dbus_method("a{sv}", "s")
    def mount(self, options: Options) -> str:
        raise NotImplementedError

    @sdbus.dbus_method("a{sv}")
    def unmount(self, options: Options):
        raise NotImplementedError
