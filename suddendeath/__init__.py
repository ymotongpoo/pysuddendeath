# -*- coding:utf-8 -*-
"""suddendeath module

suddendeath module generates "突然の死" like messages.
"""

from itertools import imap, cycle
import sys
from unicodedata import east_asian_width

codec = "utf-8"
if sys.platform == "win32":
  codec = "mbcs"

default_message = u"突然の死"

def _message_length(message):
  length = 0
  for c in imap(east_asian_width, message):
    if c == 'W':
      length += 2
    elif c == 'Na':
      length += 1

  return length


def suddendeathmessage(message):
  msg_len = _message_length(message)
  header_chars = msg_len//2+2
  footer_chars = (msg_len//2)*2+1
  footer_pattern = cycle([u"Y", u"^"])

  header = u"＿" + u"人"*header_chars + u"＿"
  footer = u"￣"
  for i in range(footer_chars):
    footer += footer_pattern.next()
  footer += u"￣"

  middle = u"＞　" + message + u"　＜"
  return u"\n".join([header, middle, footer])


def main():
  if len(sys.argv) < 2:
    message = default_message
  else:
    message = sys.argv[1]
    if sys.version_info.major == 2:
      message = message.decode(codec)

  print(suddendeathmessage(message).encode(codec))


if __name__ == '__main__':
  main()
