#! /usr/bin/env python3
# -*- coding:utf-8 -*-

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