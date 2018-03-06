#!/usr/bin/env python3
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

# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。

s = set([1,2,3])
print(s)

# 重复元素在set中自动被过滤：
s = set([1,2,3,3,3,4,5,6])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(7)
print(s)
s.add(4)
print(s)

# 通过remove(key)方法可以删除元素
s.remove(6)
print(s)

'''
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
'''
a = set([1,2,4])
b = set([1,3,4,5])
# 交集 1，4
print(a & b)
# 并集 1，2，3，4，5
print(a|b)

'''
list = [1,2,3,4,5]
a = set()
a.add([1,2,3,4,5])  # TypeError: unhashable type: 'list'
'''


# str是不变对象，而list是可变对象。
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['a', 'c', 'b']
a.sort()
print(a)
# 但是对不可变对象（如字符串） 操作时，值不会改变
# 因为 a 是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'
a = "abc"
b = a.replace('a', "A")
print("a = %s" % a)
print("a.replace('a', 'A') = %s"% a.replace('a', 'A'))
print("b = ", b)

# replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串
'''
对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

小结
    使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。
    tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
'''
# tuple 添加到dict中
t = ("房子", "车子", "票子")
l = ["房子", "车子", "票子"]
print("\ntuple t = {0}\nlist l = {1}".format(t, l))
d = {"name":"张三", "value":t}
print('d =', d)
# list 添加到dict中
d = {"name":"张三", "value":l}
print('d =', d)
print('d["value"] =', d["value"])

# tuple 添加到set中
print('\ns = set()')
s = set()
s.add(t)
print('\ts.add(t) =', s)
s = set(l)  # s = set(l)创建了新的对象覆盖了上面的s.add(t)的值
# s.add(l)
print('\ts.add(t) =', s)

t = (1,2,3)
l = [7,8,9]
print('\nt = %s\nl = %s'% (t, l))
# s.add(t)  # TypeError: unhashable type: 'list', 原因是上面s = set(l)已经声明了key的类型，而现在添加的是tuple类型
ss = set()
ss.add(t)
print(ss)

ss = set(l) # ss被赋值为新的对象
print(ss)
# s.add(l)    # TypeError: unhashable type: 'list'
print("set 对象只能add不可变对象, 否则会报TypeError错！因为set对象是key的集合，而key只能是不可变对象")

t = (1,2,3)
tt = (1, [2,3], 4)
se = set(t) # tuple t是不可变对象
print(se)
# se = set(tt)  # TypeError: unhashable type: 'list' 
# 原因：tuple tt里面有list， list是可变对象

''' 测试
    list 的格式  a=['a','b','c']
    tuple 的格式 a=('a','b','c')
    dict 的格式  a={a:b}--b可以省略 a不能为list
    set 的格式   a=set((a))--a不能为list 
    a=(1,2,3)
    b=(1, [2, 3])
    c={a}
    {(1, 2, 3)}
    这里(1,2,3)应该是一个整体的key值

    d={b}
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: unhashable type: 'list'
    dict 的key必须为不可变对象。而 b中的[2,3]可变所以报错。

    e={a:b}
    {(1, 2, 3): (1, [2, 3])}
    e[a]
    (1, [2, 3])
    dict 的key必须为不可变对象。这里将key变成了不可变对象。value是否可变无影响。
    b[1][0]=3
    e
    {(1, 2, 3): (1, [3, 3])}

    f=set(a) 
    {1, 2, 3}
    这里1,2,3表示有这三个元素，即使是显示结果排序了，也不表示set是有序的。

    g=set(b)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: unhashable type: 'list'
    set 的key必须为不可变对象。而 b中的[2,3]可变所以报错。
'''