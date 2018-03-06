#!/usr/bin/env pythons\3
# -*- conding:utf-8 -*-

# 递归函数的优点是定义简单，逻辑清晰。
# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(5))
''' 计算过程如下：
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''
# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
''' print(fact(1000))函数报错如下：
        Traceback (most recent call last):
        File "recursive_func.py", line 28, in <module>
            print(fact(1000))
        File "recursive_func.py", line 9, in fact
            return n * fact(n-1)
        File "recursive_func.py", line 9, in fact
            return n * fact(n-1)
        File "recursive_func.py", line 9, in fact
            return n * fact(n-1)
        [Previous line repeated 994 more times]
        File "recursive_func.py", line 7, in fact
            if n==1:
        RecursionError: maximum recursion depth exceeded in comparison
'''

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact_new(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num ==1:
        return product
    return fact_iter(num-1, num*product)
# return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用
print(fact_new(5))
# print(fact_new(1000))  # RecursionError: maximum recursion depth exceeded in comparison
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出!
'''
小结

    使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

    针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

    Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''
# 练习: 汉诺塔的移动可以用递归函数实现
def move(n, x, y, z):
    if n==1:
        print(x, "---->", z)
    else:
        move(n-1, x, z, y)
        move(1, x, y, z)
        move(n-1, y, x, z)
move(3, 'x', 'y', 'z')