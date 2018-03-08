#!/ysr/bin/env python3
# -*- coding:utf-8 -*-

# 给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
d = {"a":1, "b":2, "c":3}
for key in d:
    print(d[key])

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)
'''
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
默认情况下，dict迭代的是key。
如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
由于字符串也是可迭代对象，因此，也可以作用于for循环
'''
for s in "ABC":
    print(s)

# 使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print("\n判断类型isinstance(obj, type):", isinstance(d, dict))

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, v in enumerate(["A", "B", "C"]):
    print(i, v)

for x, y,z in [(1,2,3), (4,5,6), (7,8,9)]:
    print(x, y, z)

# 练习： 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L==[]:
        return (None, None)
    arr = []
    for v in L:
        arr.append(v)
    arr.sort()
    return (arr[0], arr[-1])
print(findMinAndMax([7,2,4,6,93,9,3,8]))