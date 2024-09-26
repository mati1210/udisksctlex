# SPDX-License-Identifier: MPL-2.0
import sdbus
import pathlib
import argparse
from .dbus import *


def main():
    parser = argparse.ArgumentParser("udisksctlex")
    parser.add_argument(
        "-t",
        "--dbus-timeout",
        type=int,
        default=60,
        metavar="SECS",
        help="set timeout for dbus calls, in seconds",
    )

    subparsers = parser.add_subparsers(title="commands", dest="command")

    loop_setup = subparsers.add_parser("loop-mount")
    loop_setup.add_argument(
        "file",
        help="sets-up a loop device, unlocks it, and mounts it",
        type=pathlib.Path,
    )

    args = parser.parse_args()

    bus = sdbus.sd_bus_open_system()
    bus.method_call_timeout_usec = args.dbus_timeout * 1000000
    sdbus.set_default_bus(bus)
    match args.command:
        case "loop-mount":
            from .loop_open import loop_open

            loop_open(args.file)


if __name__ == "__main__":
    main()
