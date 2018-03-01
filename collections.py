#! /usr/bin/env python3
# -*- coding:utf-8 -*-

#===================================================================================
# list是一种有序的集合，可以随时添加和删除其中的元素。
# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0！

classmates = ["Mecheal", "张三", "李四"]
print(classmates)
# 用len()函数可以获得list元素的个数
print(len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 用-1做索引，直接获取最后一个元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
# list是一个可变的有序表, 可以往list中追加元素到末尾
classmates.append("lisi")
print(classmates)
# 把元素插入到指定的位置
classmates.insert(1, "wangwu")
print(classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[2] = "lisiiii"
print(classmates)

# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(2)
print(classmates)

print("\n")
# list里面的元素的数据类型也可以不同
L = ["apple", 123, True]
print(L)

# list元素也可以是另一个list
c = ["C", "C++"]
s = ["Java", "Python", c, "PHP"]
print(s)
print(c[1])
print(s[2][1])
# =================================================================================

# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
'''
和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。

而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
需要牢记的第一条就是dict的key必须是不可变对象。这是因为dict根据key来计算value的存储位置，
如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
这个通过key计算位置的算法称为哈希算法（Hash）。要保证hash的正确性，作为key的对象就不能变。
在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
而list是可变的，就不能作为key.
'''

names = {"张三":85, "李四":90, "王武":100, "赵六":75}
print(names["李四"])

names["李四"] = 80
print(names["李四"])
names["李四"] = 65
print(names["李四"])

# 根据key取值时，如果key不存在，dict就会报错
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print("张三" in names)
print("wgh" in names)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(names.get('Thomas'))
print(names.get('Thomas', -1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
names.pop("张三")
print(names)
#==================================================================================
