# Copyright 2023 Yoshi Yamaguchi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

from . import CODEC, DEFAULT_MESSAGE, suddendeathmessage


def main():
    if len(sys.argv) < 2:
        message = DEFAULT_MESSAGE
    else:
        message = sys.argv[1]

    print(suddendeathmessage(message))


main()