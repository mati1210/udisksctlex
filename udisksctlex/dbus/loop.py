# SPDX-License-Identifier: MPL-2.0

import sdbus
from . import SERVICE_NAME, Options


class Loop(sdbus.DbusInterfaceCommon, interface_name="org.freedesktop.UDisks2.Loop"):

    def __init__(self, object_path: str, bus: sdbus.SdBus | None = None):
        super().__init__(SERVICE_NAME, object_path, bus)

    @sdbus.dbus_method("a{sv}")
    def delete(self, options: Options):
        raise NotImplementedError
