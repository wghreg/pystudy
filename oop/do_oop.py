#!/usr/bin/env python3
# -*- coding:utf-8 -*-
''' 类和实例'''
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
# 比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# Python中，定义类是通过class关键字：
class Student(object):
    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
    # 第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self, name, score):    #  注意：特殊方法“__init__”前后分别有两个下划线！！！
        self.name = name
        self.score = score
    def print_score(self):
        print("%s: %s" % (self.name, self.score))
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
# 继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

# 数据封装、继承和多态是面向对象的三大特点
# 面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的程序写出来就像这样:
bart = Student("Bart", 97)
lisa = Student("lisa", 69)
bart.print_score()
lisa.print_score()
print("bart =", bart)
print("Student =", Student)

bart = Student("abc", 80)
print("bart.name =", bart.name)
print("bart.score =", bart.score)
def print_score2(std):
    print("%s: %s" % (std.name, std.score))
print_score2(bart)
# 既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样就把“数据”给封装起来了。

class std(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print("%s: %s" % (self.name, self.score))
# bart = std("aaa", 90)
bart.print_score()

class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score>=90:
            return "A"
        elif self.score>=60:
            return "B"
        else:
            return "C"
lisa = Student2("lisa", 90)
bart = Student2("bart", 65)
print(lisa.get_grade())
print(bart.get_grade())

''' 访问限制 '''
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def set_age(self, age): # 在方法中，可以对参数做检查，避免传入无效的参数
        if 0<=age<=100:
            self.__age = age
        else:
            raise ValueError("bad age!")

    def print_score(self):
        print("%s: %s" % (self.__name, self.__age))

bart = Person("Bart", 32)
# print(bart.__name)   # AttributeError: 'Person' object has no attribute '__name'
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

# 给Student类增加get_name和get_score方法：
print("bart.get_name():", bart.get_name())
print("bart.get_age():", bart.get_age())
bart.set_age(40)
print("set_age(self, age)之后的get_age()=", bart.get_age())

# bart.set_age(120)
# print("set_age(self, age)之后的get_age()=", bart.get_age())

'''
注意: 
在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
'''
print("\nbart._Person__name =", bart._Person__name)
# 强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。Python本身没有任何机制阻止你干坏事，一切全靠自觉。

'''
注意下面的这种错误写法：
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量：
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
'''
print(bart.get_name())
bart.__name = "New Name"
print("bart.__name =", bart.__name)
print("bart.get_name() =", bart.get_name())

'''
练习: 
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
'''
print("\n测试：")
class Test(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender

# 测试:
bart = Test('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')