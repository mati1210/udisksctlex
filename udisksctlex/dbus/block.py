# SPDX-License-Identifier: MPL-2.0

import sdbus
from . import SERVICE_NAME


class Block(sdbus.DbusInterfaceCommon, interface_name="org.freedesktop.UDisks2.Block"):

    def __init__(self, object_path: str, bus: sdbus.SdBus | None = None):
        super().__init__(SERVICE_NAME, object_path, bus)

    @sdbus.dbus_property("b")
    def read_only(self) -> bool:
        raise NotImplementedError

    @sdbus.dbus_property("ay")
    def device(self) -> bytes:
        raise NotImplementedError

    @sdbus.dbus_property("s")
    def id_type(self) -> str:
        raise NotImplementedError

    @sdbus.dbus_property("s")
    def id_usage(self) -> str:
        raise NotImplementedError
