#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print(type(123))        #<class 'int'>
print(type('123'))      #<class 'str'>
print(type(None))       #<class 'NoneType'>

print(type(abs))        #<class 'builtin_function_or_method'>

class Animal(object):
    pass
a = Animal()
print(type(a))          #<class '__main__.Animal'>

print(type(123)==int)   #True

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
'''
import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
type((x for x in range(0,10)))==types.GeneratorType


使用isinstance(): 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
'''
print(type([1,2,3]))    #<class 'list'>
print(type((1,2,3)))    #<class 'tuple'>

print(isinstance([1,2,3], (list, tuple))) #True
print(isinstance((1,2,3), (list, tuple))) #True
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

#================================================================
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print("\n使用dir():\n", dir("ABC"))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len("ABC"))
print("ABC".__len__()) # "ABC".__len__ = <method-wrapper '__len__' of str object at 0x000000000211D6C0>

# 自定义
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog), dog.__len__()) # dog.__len__ = <bound method MyDog.__len__ of <__main__.MyDog object at 0x00000000021EAB70>>

print("ABC".lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x
    
myObj = MyObject()
# 获取对象属性
print(hasattr(myObj, "x"))
print(myObj.x)
print(hasattr(myObj, 'y'))
setattr(myObj, 'y', 19)
print(hasattr(myObj,"y"))
print(myObj.y)
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print("获取不存在的属性，并指定默认返回值:", getattr(myObj, "z", 404))

# 获取对象的方法
print("获取对象的方法：\n", hasattr(myObj, "power"))
print(getattr(myObj, "power"))

fn = getattr(myObj, "power")
print(fn())

'''
小结

通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
如果可以直接写：sum = obj.x + obj.y  就不要写： sum = getattr(obj, 'x') + getattr(obj, 'y')
一个正确的用法的例子如下：
'''
def readImage(fd):
    if hasattr(fd, "read"):
        return readData(fd)
    return None
'''
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。


这一章所讲的内容一般在什么时候会用到呢，我就翻了下，然后记录下来，给后面的同学做个参考。
# 首先你有一个command.py文件，内容如下，这里我们假若它后面还有100个方法

class MyObject(object):
    def __init__(self):
        self.x = 9
    def add(self):
        return self.x + self.x

    def pow(self):
        return self.x * self.x

    def sub(self):
        return self.x - self.x

    def div(self):
        return self.x / self.x

# 然后我们有一个入口文件 exec.py，要根据用户的输入来执行后端的操作
from command import MyObject
computer=MyObject()

def run():
    inp = input('method>')

    if inp == 'add':
        computer.add()
    elif inp == 'sub':
        computer.sub()
    elif inp == 'div':
        computer.div()
    elif inp == 'pow':
        computer.pow()
    else:
        print('404')

上面使用了if来进行判断，那么假若我的command里面真的有100个方法，那我总不可能写100次判断吧，所以这里我们就会用到python的反射特性，看下面的代码

from command import MyObject

computer=MyObject()
def run(x):
    inp = input('method>')
    # 判断是否有这个属性
    if hasattr(computer,inp):
    # 有就获取然后赋值给新的变量
        func = getattr(computer,inp)
        print(func())
    else:
    # 没有我们来set一个
        setattr(computer,inp,lambda x:x+1)
        func = getattr(computer,inp)
        print(func(x))

if __name__ == '__main__':
    run(10)
其实本章的内容，很多涉及到动态加载模块类，不知道为什么老师没讲，我也不知道自己说的对不对。
'''