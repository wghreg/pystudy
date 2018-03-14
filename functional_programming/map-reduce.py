#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Python内建了map()和reduce()函数:
# map()函数接收两个参数，一个是函数，一个是Iterable。 因为Iterator是惰性序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
r = map(f, [1,2,3,4,5,6,7,8,9])
print("map(function, Iterable)函数: eg. map(f, [1,2,3,4,5,6,7,8,9]) =", list(r))

L = []
for i in [1,2,3,4,5,6,7,8,9]:
    L.append(i*i)
print("等价于 for... in... [].append()：",L)
# 但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？
# 所以，map()作为高阶函数，事实上它把运算规则抽象了。
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
print("将数字列表转为字符串列表：", list(map(str, [1,2,3,4,5,6])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现：
'''
    >>> from functools import reduce
    >>> def add(x, y):
        return x+y
    >>> print("\nreduce:", reduce(add, [1,3,5,7,9]))

求和运算可以直接用Python内建函数sum()，没必要动用reduce。

但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
    >>> from functools import reduce
    >>> def fn(x, y):
    ...     return x * 10 + y
    ...
    >>> reduce(fn, [1, 3, 5, 7, 9])
    13579

这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
    >>> from functools import reduce
    >>> def fn(x, y):
    ...     return x * 10 + y
    ...
    >>> def char2num(s):
    ...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    ...     return digits[s]
    ...
    >>> reduce(fn, map(char2num, '13579'))
    13579

整理成一个str2int的函数就是：
    from functools import reduce

    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def str2int(s):
        def fn(x, y):
            return x * 10 + y
        def char2num(s):
            return DIGITS[s]
        return reduce(fn, map(char2num, s))

还可以用lambda函数进一步简化成：
    from functools import reduce

    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(s):
        return DIGITS[s]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))

也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！
lambda函数的用法在后面介绍。
'''
# 练习
# 1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()
print(normalize("aBC"))
L = ['adam', 'LISA', 'barT']
print(list(map(normalize, L)))

# 2. Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# eg. prod([3, 5, 7, 9]) == 945
from functools import reduce
def prod(L):
    return reduce(lambda x, y:x*y, L)

# 3. 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# abs(str2float('123.456') - 123.456) < 0.00001:
def str2float(s):
    int_part, dec_part = s.split('.')
    return reduce(lambda x, y: 10*x+y, map(int, int_part)) + \
           reduce(lambda x, y: 10*x+y, map(int, dec_part))*10**(-len(dec_part)) # x**y 表示x的y次幂  这里是10的-3次幂的意思
