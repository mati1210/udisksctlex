# SPDX-License-Identifier: MPL-2.0
# doc: https://storaged.org/doc/udisks2-api/latest/gdbus-org.freedesktop.UDisks2.Block.html
import sdbus
from . import SERVICE_NAME
from .types import *
from typing import TypedDict


class FormatOptions(
    TypedDict(
        "FormatOptions",
        {
            "take-ownership": VariantBool,
            "encrypt.passphrase": VariantByteArray | VariantStr,
            "encrypt.type": VariantStr,
            "mkfs-args": VariantStrArray,
            "no-block": VariantBool,
            "update-partition-type": VariantBool,
        },
        total=False,
    ),
    Options,
    total=False,
):
    uuid: VariantStr
    label: VariantStr
    erase: VariantStr


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

    @sdbus.dbus_method("sa{sv}")
    def format(self, type: str, options: FormatOptions):
        raise NotImplementedError
