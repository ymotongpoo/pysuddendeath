# -*- coding:utf-8 -*-
"""suddendeath module

suddendeath module generates "突然の死" like messages.
"""

from itertools import imap, cycle
import sys
from unicodedata import east_asian_width
import twitter
import argparse
import os
import json


codec = "utf-8"
if sys.platform == "win32":
  codec = "mbcs"

default_message = u"突然の死"

secrets_file = os.path.join(os.environ['HOME'], ".suddendeath")

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
  parser = argparse.ArgumentParser(description="suddendeath command")
  parser.add_argument('-t', '--twitter', action="store_true")
  parser.add_argument('message', action="store", nargs='?')
  args = vars(parser.parse_args())
  message = args['message']
  if message is None:
    message = default_message
  elif sys.version_info.major == 2:
    message = message.decode(codec)
  
  if not args['twitter']:
    print(suddendeathmessage(message).encode(codec))
  else:
    with open(secrets_file) as fp:
      data = json.load(fp)
      api = twitter.Api(**data)
      status = api.PostUpdate(suddendeathmessage(message).encode(codec))
      print status.text

if __name__ == '__main__':
  main()
