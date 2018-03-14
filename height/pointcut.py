#!/usr/bin/env python3
# -*- conding:utf-8 -*-

# 经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作
L = ["A", "B", "C"]
print(L[0:3])   # 0 可以省略
print(L[:3])
print(L[1:3])
print(L[1:2])
print(L[2:3])

print("\n", L[-1])    # -1标识倒数第一个
print(L[-2:-1])
print(L[-2:0])
print(L[-2:])

L = list(range(100))
print("\n%s"%L)
print(L[:10])
print(L[10:20]) # 前11-20个数
print(L[-10:])
print(L[:10:2]) # 前10个数，每两个取一个
print(L[::5])   # 所有数，每5个取一个

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print("\ntuple 切片：", (0, 1, 2, 3, 4, 5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print("\n字符串截取：", "abcdefg"[:3])
print("abcdefg"[::3])
print("abcdefg"[2::3])
print("abcdefg"[2:5:2])

# 练习，实现trim()
print("\n练习，实现trim():\n------------------------")
def trims(s):
    print(s)
    print(len(s))
    if len(s)==0:
        return None
    else:
        if s[0]==' ':
            return trims(s[1:])
        elif s[-1]==' ':
            return trims(s[:-1])
        else:
            return s
st = trims("  hello?--  ")
print(st)
print(len(st))