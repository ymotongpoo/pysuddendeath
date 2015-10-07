# coding=utf-8
from __future__ import unicode_literals
import suddendeath


def test_detect_length():
    assert 2 == len(u'한글')
    assert 7 == len(u'english')
    assert 7 == len(u'mixed두개')
    assert 7 == suddendeath._message_length(u'english')
    assert 4 == suddendeath._message_length(u'한글')
    assert 9 == suddendeath._message_length(u'mixed두개')


def test_message():
    assert u'''＿人人人人＿\n＞　test　＜\n￣Y^Y^Y￣''' == suddendeath.suddendeathmessage(u'test')
    assert u'''＿人人人人＿\n＞　한글　＜\n￣Y^Y^Y￣''' == suddendeath.suddendeathmessage(u'한글')
    assert u'''＿人人人人人人＿\n＞　testtest　＜\n￣Y^Y^Y^Y^Y￣''' == suddendeath.suddendeathmessage(u'testtest')
