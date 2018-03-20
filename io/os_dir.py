#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'小结: Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。'
import os
print("操作系统类型(posix表示linux、Unix、MaxOS, nt表示windows)：",os.name)  # posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print(os.uname()) # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print("\n获取环境变量：", os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print("\n获取某个环境变量的值：", os.environ.get("Path"))
print(os.environ.get("x", "default"))

'''
操作文件和目录
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
'''
print("\n默认目录：", os.path)  # 默认Python的安装目录
print(os.path.abspath("."))     # 文件当前目录

os.mkdir("/testdir")    # 根目录创建文件(夹), (FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: '/testdir')
os.rmdir("/testdir")    # 删除根目录文件(夹)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：part-1\part-2
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split("D:\\test.txt"))
'# 合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。'
# print(os.rename("test.txt", "test.py"))
# print(os.remove("test.py"))
'''
但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]

要列出所有的.py文件，也只需一行代码：
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

练习：
'''
# 1. 利用os模块编写一个能实现dir -l输出的程序。
# from os
print("\n练习1：", os.listdir("D:\\pyws\pystudy"))
def dir_l(path):
    for x in os.listdir(path):
        if os.path.isdir(path+"\\"+x):
            print(True)
        print("--------------", x)
dir_l("D:\\pyws\pystudy")

print(os.path.isfile('D:\\pyws\\pystudy\\.git\\COMMIT_EDITMSG'))    #True

# 2. 能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
print("\n练习2：")
# 显示目录下的
def disp(path):
    print(path.split("\\")[-1], "：", os.listdir(path))
    for x in os.listdir(path):
        if os.path.isfile(x):
            print("\t------", x)
        else:
            if os.path.isdir(path+"\\"+x):
                disp(path+"\\"+x)
            else:
                print("\t------", x)

disp("D:\pyws\pystudy")

# ==================================================================
import time
class MyLsL(object):
    def __init__(self,dir='.'):
        self.dirList=os.listdir(dir)

    def ls(self):
        fileLists=[]
        for file in self.dirList:
            print(self.getFileInfo(file))


    def getFileInfo(self,fileName):
        size = str(os.path.getsize(fileName))
        fileType = 'd' if os.path.isdir(fileName) else '-'
        readAble = 'r' if os.access(fileName,os.R_OK) else '-'
        writeAble = 'w' if os.access(fileName,os.W_OK) else '-'
        opeAble = 'x' if os.access(fileName,os.X_OK) else '-'
        timestamp = os.path.getctime(fileName)
        timeLocal = time.localtime(timestamp)
        dt = time.strftime('%Y-%m-%d',timeLocal)
        return fileType+readAble+writeAble+' '+opeAble+' '+size+' '+dt

class findFile(object):
    relativePath=''
    def __init__(self,fileName):
        self.fileName=fileName

    def showPath(self,path = '.'):
        self.relativePath = self.relativePath+path+'/'
        dirs = os.listdir(self.relativePath)
        for dir in dirs:
            if os.path.isdir(self.relativePath+dir):
                if  dir != '__pycache__':
                    self.showPath(dir)
            else:
                if dir.find(self.fileName) >= 0:
                    print(self.relativePath+dir)
        self.relativePath=''
