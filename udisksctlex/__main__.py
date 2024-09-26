# SPDX-License-Identifier: MPL-2.0

import sys
import getpass
import sdbus
from .dbus import *

sdbus.set_default_bus(sdbus.sd_bus_open_system())

is_crypto = False
manager = Manager()

with open(sys.argv[1], "a+b") as fd:
    loop_object_path = manager.loop_setup(fd.fileno(), {})

block = Block(loop_object_path)
print(f"Loop file: {block.device}")
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
