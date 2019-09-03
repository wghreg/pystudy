#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys  # 模块，sys指向这个模块对象
import inspect

import fnmatch as m

"""
__doc__: 文档字符串。如果模块没有文档，这个值是None。
*__name__: 始终是定义时的模块名；即使你使用import .. as 为它取了别名，或是赋值给了另一个变量名。
*__dict__: 包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象。
__file__: 包含了该模块的文件路径。需要注意的是内建的模块没有这个属性，访问它会抛出异常！
"""
print(m.__doc__)
print(m.__name__)
print(m.__file__)
print(m.__dict__)


class Cat(object):  # 类，Cat指向这个类对象
    """
    __doc__: 文档字符串。如果类没有文档，这个值是None。
    *__name__: 始终是定义时的类名。
    *__dict__: 包含了类里可用的属性名-属性的字典；也就是可以使用类名.属性名访问的对象。
    __module__: 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象。
    *__bases__: 直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类。
    """
    def __init__(self, name='kitty'):
        self.name = name

    def sayHi(self):  # 实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print
        self.name, 'says Hi!'  # 访问名为name的字段，使用实例.name访问


cat = Cat()  # cat是Cat类的实例对象

print(Cat.sayHi)  # 使用类名访问实例方法时，方法是未绑定的(unbound)
print(cat.sayHi)  # 使用实例访问实例方法时，方法是绑定的(bound)


cat = Cat('kitty')

print(cat.name)  # 访问实例属性
cat.sayHi()  # 调用实例方法

print(dir(cat))  # 获取实例的属性名，以列表形式返回
if hasattr(cat, 'name'):  # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger')  # same as: a.name = 'tiger'
print(getattr(cat, 'name'))  # same as: print a.name

getattr(cat, 'sayHi')()  # same as: cat.sayHi()


