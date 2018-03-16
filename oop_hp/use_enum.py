#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'使用枚举类'
'''
定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
    JAN = 1
    FEB = 2
    MAR = 3
    ...
    NOV = 11
    DEC = 12

好处是简单，缺点是类型是int，并且仍然是变量。
更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
Python提供了Enum类来实现这个功能：
'''
from enum import Enum
Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)   # value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique         # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0     # sunday的value设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print("\n自定义枚举类：")
for name, d in Weekday.__members__.items():
    print(name, '==>', d, '=', d.value)
# 获取枚举常量时，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
print("Weekday.Fri =", Weekday.Fri)
print("Weekday['Fri'] =", Weekday['Fri'])
print("Weekday(5) =", Weekday(5))

'''
练习: 
    把Student的gender属性改造为枚举类型，可以避免使用字符串：
'''
# from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 1    # 男
    Female = 0  # 女

print("\n 练习：\nGender(Gender.Male) =", Gender(Gender.Male))
print("Gender(0) =", Gender(0))

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)
bart = Student("Bart", Gender.Male);
print(bart.gender)
print(bart.gender == Gender.Male)

'''小结: Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。'''