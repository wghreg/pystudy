#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
import pytest

def test_case():
    expected = "Hello"
    actual = "hello"
    assert expected == actual

if __name__=="__main__":
    pytest.main()

报错：
    Traceback (most recent call last):
    File "test_pytest.py", line 3, in <module>
        import pytest
    ModuleNotFoundError: No module named 'pytest'
'''

import importlib
'Python自带的unittest(https://docs.python.org/3/library/unittest.html)单元测试框架就有了自己的断言方法self.assertXXX()，而且不推荐使用assert XXX语句。'
import unittest
class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FoO")

if __name__ == "__main__":
    unittest.main()

'''
我非常喜欢ptest(https://pypi.python.org/pypi/ptest)，感谢Karl大神写了这么一个测试框架。
ptest中的断言可读性很好，而且通过IDE的智能提示你能轻松完成各种断言语句。

不仅仅是你和我对Python中的断言表示不满足，所以大家都争相发明自己的assert包。
在这里我强烈推荐assertpy(https://pypi.python.org/pypi/assertpy) 这个包，它异常强大而且好评如潮。
> pip install assertpy

from assertpy import assert_that

def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar')\
        .is_length(6)\
        .starts_with('foo')\
        .ends_with('bar')
    assert_that(['a', 'b', 'c'])\
        .contains('a')\
        .does_not_contain('x')
从它的github(https://github.com/ActivisionGameScience/assertpy) 主页 文档上你会发现它支持了几乎你能想到的所有测试场景，包括但不限于以下列表。

Strings
Numbers
Lists
Tuples
Dicts
Sets
Booleans
Dates
Files
Objects
而且它的断言信息简洁明了，不多不少。
    Expected <foo> to be of length <4>, but was <3>.
    Expected <foo> to be empty string, but was not.
    Expected <False>, but was not.
    Expected <foo> to contain only digits, but did not.
    Expected <123> to contain only alphabetic chars, but did not.
    Expected <foo> to contain only uppercase chars, but did not.
    Expected <FOO> to contain only lowercase chars, but did not.
    Expected <foo> to be equal to <bar>, but was not.
    Expected <foo> to be not equal to <foo>, but was.
    Expected <foo> to be case-insensitive equal to <BAR>, but was not.
'''
