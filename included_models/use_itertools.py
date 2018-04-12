#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
首先，我们看看itertools提供的几个“无限”迭代器：
'''
import itertools
natuals = itertools.count(1)
'''
# 1. count()
# 无限循环
for n in natuals:
    print(n)

因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

cycle()会把传入的一个序列无限重复下去：

# 2. cycle()
cs = itertools.cycle("abc")
for n in cs:
    print(n)
'''
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
# 3. repeat(obj, times)
'''
ns = itertools.repeat("a", 3)
for n in ns:
    print(n)

无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
'''
ns = itertools.takewhile(lambda x:x<=10, natuals)
print(list(ns))    # [1,2,3,4,5,6,7,8,9,10]

# 4. chain(str1, str2)
for c in itertools.chain("abc", "xyz"):
    print(c)
print(list(itertools.chain("abc", "xyz")))

# 5. groupby() 把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby("AAABBBCCCDDEEESSSDAVAV"):
    print(key, list(group))
'''
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
'''
print("\ngroupby(strobj, func或lambda表达式)：")
for key, group in itertools.groupby("AAaaBBbcCCAAa", lambda c:c.upper()):
    print(key, list(group))

'''
练习

计算圆周率可以根据公式：
    利用Python提供的itertools模块，我们来计算这个序列的前N项和：
'''
# import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_num = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_list = []
    ns = itertools.takewhile(lambda x:x<=2*N-1, odd_num)
    for i in ns:
        odd_list.append(i)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    n = 0
    j = 0
    while n<len(odd_list):
        if n%2 !=0:
            odd_list[n] = -odd_list[n]
        j += 4/odd_list[n]
        n+=1
    # step 4: 求和: return 3.14
    return j

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


def get_pi(N):
    '计算pi的值'
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_N = list(itertools.islice(odds, 0, N))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    map(lambda x:4/x, list(map(lambda a, b:a*b, odd_N, list(itertools.islice(itertools.cycle([1, -1]), 0, N)))))
    # step 4: 求和:
    return sum(map(lambda x:4/x, list(map(lambda a,b:a*b, odd_N, list(itertools.islice(itertools.cycle([1,-1]), 0, N))))))

print("get_pi(10) =",get_pi(10))


import math
def getpi(N):
    s =1
    pi = 0
    for x in itertools.takewhile(lambda x:x<=2*N-1, itertools.count(1,2)):
        s +=1
        pi += math.pow(-1, s)*4/x
    return pi
print("getpi(10) =", getpi(10))