# SPDX-License-Identifier: MPL-2.0

import sys
import getpass
import sdbus
import pathlib
from .dbus import *

# TODO: proper error checking (make sure to delete loop file even if error occured, etc)


def loop_open(file: pathlib.Path):
    is_crypto = False
    manager = Manager()

    with open(file, "a+b") as fd:
        loop_object_path = manager.loop_setup(fd.fileno(), {})

    block = Block(loop_object_path)
    print(
        f"Loop file: {str(block.device, encoding='utf-8', errors='backslashreplace')}"
    )
    if block.id_usage == "crypto":
        is_crypto = True
        crypt = Encrypted(loop_object_path)
        while True:
            try:
                crypt_object_path = crypt.unlock(getpass.getpass(), {})
                break
            except sdbus.SdBusUnmappedMessageError as e:
                print(f"Failed to unlock device! {e}")
                pass

        object_path = crypt_object_path
    else:
        object_path = loop_object_path

    fs = Filesystem(object_path)
    mount_path = fs.mount({})
    print(f"Mounted at {mount_path}.")

    input("Enter to dismount.")

    print(f"Trying to unmount {mount_path}...", end="")
    while True:
        try:
            fs.unmount({})
            break
        except:
            pass
    print("Unmounted.")
    if is_crypto:
        crypt.lock({})

    Loop(loop_object_path).delete({})
