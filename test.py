#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'测试'

# 实现trim()去掉字符串左右空格
def trim(s):
    if s[0]!=' ' and s[-1]!=' ':
        print(s)
    if s[0]==' ':
        return trim(s[1:])
    if s[-1]==' ':
        return trim(s[:-1])
s=str(input("请输入字符串："))
trim(s)

print("\ntuple类型给多参数赋值，注意：")
a = 3
a, b = 1, a
print("a =", a, "\nb =", b)

# 但是， 实验证明 max,min = min ,max 这条语句 并不等价于 顺序执行 max = min , min =max 而是同时执行···
max, min = min, max
print(max(1, 2, 3, 4, 5)) # -> 结果是1
print(min(1, 2, 3, 4, 5)) # -> 结果是5
max=min
print(max(1,2,3,4,5))   # 结果是5
print(min(1,2,3,4,5))   # 结果也是5

'''
max,min=min,max
对于这个不等价于max=min,min=max，如果你有印象的话，其实在前文"高级特性-生成器"那篇文章中,廖老师有专门拿出来提到过的，
就是使用非递归循环方式编写的斐波那契数列中有一步就与此类似，即：
a,b=b,a+b
这里等号右边实际上是一个tuple，因此等号右边的a在定义的时候就已经确定了，并不会因为将b赋值给了左边的a而改变
'''

t = ("Bob", 75)
print(t[0])