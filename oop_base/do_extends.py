#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
'''
小结

继承可以把父类的所有功能都直接拿过来，这样就不必重零做起(继承)，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写(多态)。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

'''
class Animal(object):
    def run(self):
        return "animal is running......"

class Cat(Animal):
    def run(self):
        return "Cat is running......"

    def eat(self):
        return "Cat is eating..."

class Dog(Animal):
    def run(self):
        return "Dog is running...."

    def eat(self):
        return "Dog is eating..."

dog = Dog()
cat = Cat()
print(cat.run(), cat.eat())
print(dog.run(), dog.eat())