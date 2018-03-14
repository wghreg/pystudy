#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。本质上，decorator就是一个返回函数的高阶函数。
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print("2018-03-08")
f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

print("\n添加装饰器：")
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的 @ 语法，把decorator置于函数的定义处：
# 把 @log 放到new_now()函数的定义处，相当于执行了语句：new_now = log(new_now)
@log
def new_now():
    print("2018-03-08")
new_now()
# 由于log()是一个decorator，返回一个函数，所以原来的new_now()函数仍然存在，只是new_now变量指向了新函数，调用new_now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
print("\n自定义log文件：")
def def_log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@def_log("execute the function")
def p_now():
    print("2018-03-08")
p_now()
'''
和两层嵌套的decorator相比，3层嵌套的效果是这样的：>>> now = log('execute')(now)
首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
>>> now.__name__
'wrapper'
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

import functools
def log3(func):
    @functools.wraps
    def wrapper(*args, **kw):
        print("call the funcation %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

# log3(now)

或者针对带参数的decorator：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。
'''
# 练习: 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
from collections import namedtuple
import time,functools
def metric(func):
    def wrapper(*args, **fw):
        print("%s execute in %s ms" % (func.__name__, 10.24))
        return func(*args, **fw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x+y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x*y*z

f = fast(11,22)
s = slow(11,22,33)

'''
小结

在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：
@log('execute')
def f():
    pass

==========================================================
def log(arg):
    def inner_log(text='call'):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

    if callable(arg):
        return inner_log()(arg)
    return inner_log(arg)

@log
def f():
    pass

@log('execute')
def f2():
    pass

f()  # call f():
f2()  # execute f2():

==========================================================

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t0 = time.time()
        result = fn(*args, **kw)
        print('%s executed in %.4f ms' % (fn.__name__, time.time() - t0))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

fast(11, 22)  # fast executed in 0.0017 ms
slow(11, 22, 33)  # slow executed in 0.1281 ms

==========================================================

def log(x):
    def decorator(f):
        if isinstance(x,str):
            text=x
        else:
            text='call'
        def wrapper(*args,**kw):
            print("%s %s()"%(text,f.__name__))
            return f(*args,**kw)
        return wrapper
    if isinstance(x,str):
        return decorator
    return decorator(x)

==========================================================

练习: 
1. 可作用于任何函数上，并打印该函数的执行时间
import functools,time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(arg, **kw):
        s = time.time()
        fn(arg, kw)
        print('excute %s() used %.3fs' % (fn.name,(time.time() - s)))
        return fn(*arg, kw)
    return wrapper

2. 在函数调用的前后打印出'begin call'和'end call'的日志
import functools,time

def add_beginandend(func):
    print('begin call')
    @functools.wraps(func)
    def wrapper():
        func()
        print('end call')
    return wrapper        

@add_beginandend 
def g():
    print('excuting g()')

g()    

3. 同时支持 @log,@log('execute')
import types, functools

def log(n):
    # 如果参数为函数，装饰后，返回传入的函数，返回类型为Function
    if type(n) == types.FunctionType:
        print('Call %s()' % n.__name__)
        return n

    # 如果参数为字符串，返回log.decorator
    def decorator(func):
        # 装饰后，返回传入的参数，返回类型为Function
        def wrapper2():
            print('%s %s()' % (n, func.__name__))
            return func
        return wrapper2() 
    return decorator

@log    # f1 = log(f1)  
def f1():
    pass

@log('excute') # f2 = log('excute')(f2) 
def f2():
    pass

f1()
f2() 
'''