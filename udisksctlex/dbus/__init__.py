# SPDX-License-Identifier: MPL-2.0

import sdbus

SERVICE_NAME = "org.freedesktop.UDisks2"
Options = dict[str, tuple[str, any]]

from .block import Block
from .manager import Manager
from .encrypted import Encrypted
from .filesystem import Filesystem
from .loop import Loop
