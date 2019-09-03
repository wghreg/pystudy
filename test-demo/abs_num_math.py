#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def factorial(num):
    """
        在讲解本章节的内容之前，我们先来研究一道数学题，请说出下面的方程有多少组正整数解。
            $$x_1 + x_2 + x_3 + x_4 = 8$$

    求阶乘

    :param num: 非负整数
    :return: num的阶乘
    """
    result = 1
    for n in range(1, num + 1):
        result *= n

    print("result = %s" % result)
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(factorial(m) // factorial(n) // factorial(m - n))

'''
**说明：**Python的math模块中其实已经有一个factorial函数了，事实上要计算阶乘可以直接使用这个现成的函数而不用自己定义。
下面例子中的某些函数其实Python中也是内置了，这里为了讲解函数的定义和使用才把它们又实现了一遍，实际开发中不建议做这种低级的重复性的工作。
'''
