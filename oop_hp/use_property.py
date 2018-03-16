#!/usr/bin.env python3
# -*- coding:utf-8 -*-
'''
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

s = Student()
s.score = 9999
这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
'''
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer")
        if score<0 or score >100:
            raise ValueError("score must between 0 and 100")
        self._score = score

s = Student()
s.set_score(87)
# s.set_score(999)    # ValueError: score must between 0 and 100
print(s.get_score())

# 装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
print("\n使用装饰器@property将方法变成属性，再用 @属性.setter变成属性赋值：")
class Person(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer")
        if score<0 or score >100:
            raise ValueError("score must between 0 and 100")
        self._score = score
'''
@property的实现比较复杂，先使用。
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，就拥有一个可控的属性操作：
'''
p = Person()
p.score = 60
print(p.score)
'''
@property表示该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
'''
class Code(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, birth):
        self._birth = birth
    
    @property
    def age(self):
        return 2018 - self._birth
# birth是可读写属性， age是只读属性
c = Code()
c.birth = 1989
print("获取只读属性：", c.age)

'''
小结:
@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

练习:
    请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height
    
    @property
    def resolution(self):
        return self._width * self._height

sc = Screen()
sc.width = 1024
sc.height = 768
print("练习答案：screen.resolution =", sc.resolution)