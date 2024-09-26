# SPDX-License-Identifier: MPL-2.0
# doc: https://storaged.org/doc/udisks2-api/latest/gdbus-org.freedesktop.UDisks2.Encrypted.html
import sdbus
from . import SERVICE_NAME, Options


class Encrypted(
    sdbus.DbusInterfaceCommon, interface_name="org.freedesktop.UDisks2.Encrypted"
):

    def __init__(self, object_path: str, bus: sdbus.SdBus | None = None):
        super().__init__(SERVICE_NAME, object_path, bus)

    @sdbus.dbus_method("sa{sv}", "o")
    def unlock(self, passphrase: str, options: Options) -> str:
        raise NotImplementedError

    @sdbus.dbus_method("a{sv}")
    def lock(self, options: Options):
        raise NotImplementedError
