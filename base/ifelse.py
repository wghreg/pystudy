#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断
age = 20
if age>=18:
    print("your age is", age, " & you are adult!")
else:
    print("teenager")

print("\nelif判断:")
# elif 多情况判断
age = 3
if age >= 18:
    print("adult")
elif age > 6:
    print("student")
else:
    print("baby")

# if语句执行有个特点，它是从上往下判断，
# 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age > 6:
    print("Teenager")
elif age >= 18:
    print("Adult")
else:
    print("Kid")

# if判断条件还可以简写
# 只要判断条件是非零数值、非空字符串、非空list等，就判断为True，否则为False
age = 20
if 18> age > 6:
    print("Teenager")
elif age >= 18:
    print("Adult")
else:
    print("Kid")