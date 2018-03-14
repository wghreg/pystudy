#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student2(object):
    def __init__(self, name):
        self.name = name

s = Student2("bob")
print(s.name)

class Student(object):
    name = 'Student'

s = Student()       # 创建实例s
print(s.name)       # Student 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性

print(Student.name) # Student 打印类的name属性

s.name = 'Michael'  # 给实例绑定name属性
print(s.name)       # Michael 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性

print(Student.name) # Student 但是类属性并未消失，用Student.name仍然可以访问

del s.name          # 如果删除实例的name属性
print(s.name)       # Student 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

# 不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

'''
练习:
    为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
'''
# Test.count 设置类的属性，所有实例共享属性
class Test(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Test.count = Test.count+1

# 测试
if Test.count !=0:
    print("测试失败！")
else:
    bart = Test("Bart")
    if Test.count !=1:
        print("测试失败！")
    else:
        lisa = Test("Lisa")
        if Test.count !=2:
            print("测试失败！")
        else:
            print("Test.count =", Test.count)
            print("测试成功！")