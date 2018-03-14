#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 函数作为返回值
'''
小结:
    一个函数可以返回一个计算结果，也可以返回一个函数。
    返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''
# 实现一个可变参数的求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_calc_sum(1,2,3,4,5)
print("调用lazy_calc_sum(*args)时返回一个函数f：", f)
print("调用上面返回的函数f()时，才会得到计算结果：", f())
# 在这个例子中，函数lazy_calc_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_calc_sum的参数和局部变量，当lazy_calc_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。但注意一点，当我们调用lazy_calc_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_calc_sum(1,2,3,4,5)
f2 = lazy_calc_sum(1,2,3,4,5)
print("每次调用都会返回一个新的函数，即使传入相同的参数：", f1 == f2) # False

'''
闭包:
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()    # 预期结果：1，4，9，但是最终结果都是9
print("\n返回的函数引用了变量i，但它并非立刻执行, 而是调用返回的函数时才获取变量:f1=",f1(), "f2=",f2(), "f3=",f3())
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 也就是说等调用返回的函数时， 变量i的值已经是3了
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# 缺点是代码较长，可利用lambda函数缩短代码。
def count2():
    def f(i):
        def g():
            return i*i
        return g
    fs=[]
    for j in range(1,4):
        fs.append(f(j))
    return fs
f1, f2, f3 = count2()
print("用返回函数的参数绑定变量值，变量再改变也不会影响返回函数的结果：f1=",f1(), "f2=",f2(), "f3=",f3())

# 练习  利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    s = [0]
    def counter():
        s[0] = s[0]+1
        return s[0]
    return counter
c1 = createCounter()
print("\n练习：实现一个递增计数器：", c1(),c1(),c1(),c1(),c1())
# 整个过程只调用了一次creteCounter，就是counterA = createCounter(), s也就只初始化了一次
# 此时counterA得到的是createCounter内部返回的counter函数，
# 以后每次counterA在执行的时候执行的都是counter()函数，所以整个过程createCounter就只调用了一次
