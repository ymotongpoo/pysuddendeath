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

import pytest


class Test_message_length:
    @pytest.fixture
    def target(self):
        from suddendeath import message_length
        return message_length

    @pytest.mark.parametrize("test_input, expected", [
        ("突然の死", 8),
        ("한글", 4),
        ("english", 7),
        ("git入門", 7),
        ("mixed두개", 9),
    ])
    def test_detect_length(self, test_input, expected, target):
        result = target(test_input)
        assert result == expected


class Test_suddendeathmessage:
    @pytest.fixture
    def target(self):
        from suddendeath import suddendeathmessage
        return suddendeathmessage

    @pytest.mark.parametrize("test_input, expected", [
        ("test", "＿人人人人＿\n＞　test　＜\n￣Y^Y^Y￣"),
        ("ほげ", "＿人人人人＿\n＞　ほげ　＜\n￣Y^Y^Y￣"),
        ("git入門", "＿人人人人人＿\n＞　git入門　＜\n￣Y^Y^Y^Y￣")
    ])
    def test_random_messages(self, test_input, expected, target):
        result = target(test_input)
        assert result == expected
