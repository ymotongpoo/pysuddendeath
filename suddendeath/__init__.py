# -*- coding:utf-8 -*-
"""suddendeath module

suddendeath module generates "突然の死" like messages.
"""

from itertools import cycle

import sys
from unicodedata import east_asian_width

CODEC = "utf-8"
if sys.platform == "win32":
    CODEC = "mbcs"

DEFAULT_MESSAGE = "突然の死"


def message_length(message):
    '''
    message_length returns visual length of message.
    Ascii chars are counted as 1, non-asciis are 2.

    :param str message: random unicode mixed text
    :rtype: int
    '''
    length = 0
    for char in map(east_asian_width, message):
        if char == 'W':
            length += 2
        elif char == 'Na':
            length += 1

    return length


def suddendeathmessage(message):
    '''
    suddendeathmessage returns "突然の死" like ascii art decorated message string.

    :param str message: random unicode mixed text
    :rtype: str
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


def main():
    if len(sys.argv) < 2:
        message = DEFAULT_MESSAGE
    else:
        message = sys.argv[1]
        if sys.version_info.major == 2:
            message = message.decode(CODEC)

    print((suddendeathmessage(message).encode(CODEC)))


if __name__ == '__main__':
    main()
