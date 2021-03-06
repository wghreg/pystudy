#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'排序'
'''
小结
    sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
    执行过程：把源数据经过函数处理之后再排序
'''
# 无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
# Python内置的sorted()函数就可以对list进行排序：
L = [36, 5, -21, 9, 27, -15]
print("sorted(L) =", sorted(L))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：
print("sorted(L, key=abs) =", sorted(L, key=abs))

'''
    对字符串排序
'''
S = ['bob', 'about', 'Zoo', 'Credit']
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面:
print("\n默认对字符串的排序，是按照ASCII的大小进行比较:", sorted(S))
# 排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
print("排序忽略大小写key=str.lower，按照字母序排序:", sorted(S, key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True。
print("反向排序, 可以传入第三个参数reverse=True:", sorted(S, key=str.lower, reverse=True))

"""
    练习: 用一组tuple表示学生名字和成绩, 用sorted()按名字排序：
""" 
TL = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(tup):
    return tup[0]
print(sorted(TL, key=by_name))   # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
# 按成绩从高到低排序：
def by_score(tup):
    return tup[1]
print(sorted(TL, key=by_score))  # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]

# lambda 表达式：
print(sorted(TL, key=lambda x:x[0]))
print(sorted(TL, key=lambda x:x[1]))