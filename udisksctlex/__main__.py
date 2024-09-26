# SPDX-License-Identifier: MPL-2.0
import sdbus
import pathlib
import argparse
from .dbus import *


def main():
    sdbus.set_default_bus(sdbus.sd_bus_open_system())

    parser = argparse.ArgumentParser("udisksctlex")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    loop_setup = subparsers.add_parser("loop-mount")
    loop_setup.add_argument(
        "file",
        help="sets-up a loop device, unlocks it, and mounts it",
        type=pathlib.Path,
    )

    args = parser.parse_args()

    match args.command:
        case "loop-mount":
            from .loop_open import loop_open

            loop_open(args.file)


if __name__ == "__main__":
    main()
