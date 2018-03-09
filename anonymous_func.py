#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
print(list(map(lambda x: x*x, [1,2,3,4,5,6,7,8,9])))
'''
匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
f = lambda x:x*x
print("匿名函数赋值给变量：f =",f)
print("此时变量f的值类型是函数，调用变量并传入参数：f(5) =",f(5))

# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda:x*x + y*y
f = build(3,5)
print(f)
print(f())

'''
练习：将下面的函数改为匿名函数：
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
'''
L = list(filter(lambda n:n%2==1, range(1,20)))
print("练习：将函数改为匿名函数 = ",L)

'''
def _not_divisible(n):
    return lambda x: x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n), it)
如果改成
        it=filter(lambda x: x%n>0, it)
结果就是错的，请问这是什么原因呢？

    def _not_divisible(n):
        return lambda x: x%n>0
    这里面 n 是函数参数，如果这样写 it=filter(lambda x: x%n>0, it) 就变成x是函数参数了

要想这么写,得这样 it = filter(lambda n: lambda x: x % n > 0, it) 
'''