#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A):
    pass

class C2(B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()