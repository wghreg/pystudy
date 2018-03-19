#!/usr/bin/env python3
# -*- coding:utf-8 -*-
try:
    print("try...")
    r = 10/0
    print("result =", r)
except ZeroDivisionError as e:
    print("Exception:", e)
finally:
    print("finally...")

# 没有错误发生，except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。
print("\n同时捕获多种错误及else处理：")
try:
    print("try....")
    r = 10/int('2')     # int()函数可能会抛出ValueError，用except捕获ValueError，ZeroDivisionError。
    print("result = ", r)
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as ze:
    print("ZeorDivisionError:", ze)
else:                   # 在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
    print("no error!")
finally:
    print("finally...")

'''
Python的错误其实也是class，所有的错误类型都继承自BaseException，
所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
'''
print("\nPython的错误其实也是class，所有的错误类型都继承自BaseException:")
print("存在继承关系的错误类，会被父类拦截")
def foo():
    r = abs(-2)   #some_func()
    if r==(-1):
        return (-1)
    return r

try:
    foo()
except ValueError as e:
    print("ValueError")
except UnicodeError as e:   # ValueError 是unicodeError的父类
    print("UnicodeError")
'''
第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
'''
print("\n不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就行！")
def foo2(s):
    return 10/int(s)

def bar(s):
    return foo2(s)*2
'''
def test():
    bar("0")

test()
#
    Traceback (most recent call last):      # 告诉我们错误的跟踪信息
    File "do_try.py", line 64, in <module>  # 调用main()出错了，在代码文件err.py的第64行代码
        test()
    File "do_try.py", line 62, in test      # 但原因是第62行, 调用bar('0')出错了
        bar("0")
    File "do_try.py", line 59, in bar       # 第59行代码，原因是return foo(s) * 2这个语句出错了
        return foo2(s)*2
    File "do_try.py", line 56, in foo2      #原因是return 10 / int(s)这个语句出错了，这是错误产生的源头
        return 10/int(s)
    ZeroDivisionError: division by zero
'''
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
def main():
    try:
        bar('0')
    except Exception as e:
        print("Error: ", e)
    finally:
        print("finally...")
    print("END")
main()