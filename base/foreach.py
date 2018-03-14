#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来,
# python还提供了 range()函数，可以生成一个整数序列，再通过list()函数可以转换为list;
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。

# 不要滥用break和continue语句。
# break和continue会造成代码执行逻辑分叉过多，容易出错。
# 大多数循环并不需要用到break和continue语句， 
# 可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

names = ["张三", "李四", "王武"]
for name in names:
    print(name)

print("\n10以内的整数求和：")
sum = 0
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+i
print(sum)

# range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))
sum = 0
for i in range(101):
    sum = sum+i
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 99
while n>0:
    sum = sum+n
    n = n-1
print(sum)

# 练习
print("\n练习：")
L = ["张三", "李四", "王武"]
for i in L:
    print("Hello, %s" % i)


# 在循环中，break语句可以提前退出循环
print("\nbeak 提前退出循环：")
n = 1
while n<=100:
    if n>10:
        break
    print(n)
    n = n+1
print("END")


# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
print("\ncontinue 跳过此次循环，直接开始下一次循环：")
n = 0
while n<10:
    n = n+1
    if n%2 ==0:
        continue
    print(n)