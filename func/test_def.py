#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import math
'''
    定义默认参数要牢记一点：默认参数必须指向不变对象!
'''
def add_end(L=[]):
    L.append("END")
    return L

print(add_end([1,2,3])) #[1, 2, 3, 'END']
print(add_end())    #['END']
print(add_end())    #['END', 'END']
print(add_end())    #['END', 'END', 'END']
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。


print("\n参数初始化为None，函数中判断是否为空：")
# 参数初始化为None，函数中判断是否为空
def add_end2(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

print(add_end2([1,2,3]))    #['END']
print(add_end2())    #['END', 'END']
print(add_end2())    #['END', 'END', 'END']
