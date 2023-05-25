# -*- coding:utf-8 -*-
#    Copyright 2017 Yoshi Yamaguchi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""suddendeath module

suddendeath module generates "突然の死" like messages.
"""

import sys
from itertools import cycle
from unicodedata import east_asian_width

__version__ = "0.5.2"

CODEC = "utf-8"
if sys.platform == "win32":
    CODEC = "mbcs"

DEFAULT_MESSAGE = "突然の死"


def message_length(message: str) -> int:
    '''
    message_length returns visual length of message.
    Ascii chars are counted as 1, non-asciis are 2.
    '''
    length = 0
    for char in map(east_asian_width, message):
        if char == 'W':
            length += 2
        elif char == 'Na':
            length += 1

    return length


def suddendeathmessage(message: str) -> str:
    '''
    suddendeathmessage returns "突然の死" like ascii art decorated message string.
    '''
    msg_len = message_length(message)
    header_len = msg_len // 2 + 2
    footer_len = (msg_len // 2) * 2 + 1
    footer_pattern = cycle(["Y", "^"])

    header = "＿" + "人" * header_len + "＿"
    footer = "￣"
    for _ in range(footer_len):
        footer += next(footer_pattern)
    footer += "￣"

    middle = "＞　" + message + "　＜"
    return "\n".join([header, middle, footer])


