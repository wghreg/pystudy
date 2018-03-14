#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print(list(range(11)))
print(list(range(1,11)))

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
L = []
for i in range(1, 11):
    L.append(i*i)
print(L)
# 循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
print("=[x*x for x in range(1,11)] =", [x*x for x in range(1,11) ])

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print("\n生成时添加过滤条件：", [x*x for x in range(1,11) if x%2==0])

# 使用两层循环，可以生成全排列：
print("\n两层循环：", [m + n for m in "ABC" for n in "XYZ"])

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os   # 导入os模块，模块的概念后面讲到
print("\n当前目录下的所有文件和目录名:\n", [d for d in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {"a":1, "b":2, "c":3}
for k, v in d.items():
    print(k, "=", v)
# 列表生成式也可以使用两个变量来生成list:
# print([k+" = "+v for k, v in d.items()])    # TypeError: must be str, not int
di = {"A":"X", "B":"Y", "C":"Z"}
print("列表生成式也可以使用两个变量来生成list:", [k + " = "+ v for k,v in di.items()])

li = ["Hello", "World", "Oldtie"]
print("\nlist中所有item首字母转小写：", [s.lower() for s in li])

'''
练习

如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错:
    L = ['Hello', 'World', 18, 'Apple', None]
    >>> [s.lower() for s in L]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in <listcomp>
    AttributeError: 'int' object has no attribute 'lower'
使用内建的isinstance函数可以判断一个变量是不是字符串!
'''
L1 = ["Hello", "Abc", 123, "XYZ", "World"]
print([s.lower() for s in L1 if isinstance(s, str)])