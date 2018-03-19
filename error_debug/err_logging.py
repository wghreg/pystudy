#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
记录错误

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

小结
    Python内置的try...except...finally用来处理错误十分方便。
    出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

    程序也可以主动抛出错误，让调用者来处理相应的错误。
    但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。

Python内置的logging模块可以非常容易地记录错误信息：
'''
print("同样是出错，但程序打印完错误信息后会继续执行，并正常退出：")
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar("0")
    except Exception as e:
        logging.exception(e)
main()
print("END")
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
'''
抛出错误

因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
'''
print("\n用raise语句抛出一个错误的实例:")
class FooError(ValueError):
    pass
def foo2(s):
    n = int(s)
    if n==0:
        raise FooError("invalid Value: %s" % s)
    return 10/n
# foo2("0")
'''
Traceback (most recent call last):
  File "err_logging.py", line 40, in <module>
    foo2("0")
  File "err_logging.py", line 38, in foo2
    raise FooError("invalid Value: %s" % s)
__main__.FooError: invalid Value: 0
'''
# 只在必要时才自定义错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

print("\n捕获异常后再抛出(raise): ")
def foo3(s):
    n = int(s)
    if n==0:
        raise ValueError("invalid Value： %s" % s)
    return 10/n
def bar3():
    try:
        foo3("0")
    except ValueError as e:
        print("ValueError!!!")
        raise
# bar3()
'''
ValueError!!!
Traceback (most recent call last):
  File "err_logging.py", line 55, in <module>
    bar3()
  File "err_logging.py", line 51, in bar3
    foo3("0")
  File "err_logging.py", line 47, in foo3
    raise ValueError("invalid Value： %s" % s)
ValueError: invalid Value： 0
'''
'''
这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。
但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
好比一个员工处理不了问题时，就把问题抛给老板，如果老板也处理不了，往上抛，最终会抛给CEO去处理。

raise语句如果不带参数，就会把当前错误原样抛出。
此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
'''
print("\nraise语句如果不带参数，就会把当前错误原样抛出。还可以把一种类型的错误转化成另一种类型：")
try:
    10/0
except ZeroDivisionError:
    raise ValueError("input error!")
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。

'''
练习

运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
    from functools import reduce

    def str2num(s):
        return int(s)

    def calc(exp):
        ss = exp.split('+')
        ns = map(str2num, ss)
        return reduce(lambda acc, x: acc + x, ns)

    def main():
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)

    main()
'''
def str2num(s):
    if "." in s:
        return float(s)
    else:
        return int(s)

def str2num2(s):
    try:
        return int(s)
    except ValueError:
        return float(s)