#!/usr/bin/env python3
# -*- coding:utf-8 -*-

d = {"张三":80, "李四":90, "王武":95, "赵六":87, "hanmei":66}
print("打印学生成绩单：%s" % d)

name = input("请输入要查询的学生名称：")
if name in d:
    print("%s学生的成绩为%d"% (name, d[name]))
else:
    print("您查询的学生不存在！")
    print("是否添加该学生？(y/n):")
    a = input()
    if a=='y':
        print("请录入该学生的成绩：")
        s = input()
        d[name] = int(s)
        print(d)
    else:
        print("再见！")