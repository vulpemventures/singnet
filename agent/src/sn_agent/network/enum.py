#
# sn_agent/enum.py - defines common enumerations for singNET.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from enum import Enum

class NetworkStatus(Enum):
    STATUS_NON_MEMBER = 0
    STATUS_MEMBER = 1
    STATUS_FORMER_MEMBER = 2
