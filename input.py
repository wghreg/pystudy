#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# input()返回的数据类型是str，
# str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情.
# int()函数发现一个字符串并不是合法的数字时就会报错!
s = input("birth:")
birth = int(s)
if birth <1990:
    print("90前")
elif 1990<birth<2000:
    print("90后")
else:
    print("00后")