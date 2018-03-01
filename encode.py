print("包含中文的str")

print(ord('A')) #65
print(ord("中")) # 20013

print(chr(66)) # B
print(chr(25991)) # 文

# 如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')