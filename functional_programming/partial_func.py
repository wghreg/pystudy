#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# functools.partial就是帮助我们创建一个偏函数的
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
'''
小结
    当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''
# 通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：
print("int(s, base=N)表示将传入的参数从N进制数转为10进制！")
print("int()提供额外的base参数，默认为10：", int('12345'))     # 12345
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print("base参数值为8：", int('12345', base=8))
print("base参数值为16：", int('12345', base=16))

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
print("\n封装int函数为 int2(s, base=2):")
def int2(s, base=2):
    return int(s, base)
print(int2('1000000'))
print(int2('1010101'))

print(int2('1000000', base=10))

'''
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
    import functools
    int2 = functools.partial(int, base=2)
    print(int2('1000000'))
    print(int2('1010101'))

创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：int2 = functools.partial(int, base=2) 
实际上固定了int()函数的关键字参数base，也就是：int2('10010') 
相当于：
kw = { 'base': 2 }
int('10010', **kw)

当传入：max2 = functools.partial(max, 10) 实际上会把10作为*args的一部分自动加到左边，也就是：max2(5, 6, 7) 相当于：
args = (10, 5, 6, 7)
max(*args)
结果为10。
'''

# 自己实现一个偏函数
class partial:
    def __new__(cls, func, *args, **kwargs):
        if not callable(func):
            raise TypeError("the first argument must be callable!")
        self = super().__new__(cls)
        self.func = func
        self.args = args
        self.kwargs = kwargs
        return self
    def __call__(self, *args, **kwargs):
        return self.func(*self.args, *args, **self.kwargs, **kwargs)

# 使用
def add(x, y):
    return x+y
inc = partial(add, y=1)
print(inc(41))      # 42