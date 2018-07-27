#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/27 0027 上午 11:45

import os
import zipfile
from zipfile import ZipFile

# 读取压缩文件
def print_file(inputfile_path):
    myzip = ZipFile(inputfile_path, 'r')
    for file_name in myzip.namelist():
        for data in myzip.open(file_name, 'r'):
            print(data)
    myzip.close()


# 压缩目录
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname): #判断压缩目录是否是文件，是则添加到文件列表filelist中
        filelist.append(dirname)
    else:
        for root,dirs,files in os.walk(dirname): #root是根目录,dirs存放的是子目录，files存放的是根目录下边的文件
            for name in files:
                filelist.append(os.path.join(root,name))
    zf = zipfile.ZipFile(zipfilename,"w",zipfile.ZIP_DEFLATED,allowZip64=True)
    for tar in filelist:
        arcname = tar[len(dirname):] #文件名
        zf.write(tar,arcname)  #将tar源文件的内容写到arcname文件中
    zf.close()


# 解压文件
def unzip_dir(zipfilename):
    fullzipfilepath = os.path.abspath(zipfilename)  #压缩文件的绝对路径C:\Users\Administrator\Desktop\apk数据\2017-9-1.zip
    print(fullzipfilepath)
    unzipdir = fullzipfilepath.split('.zip')[0][0:] #解压文件的根目录C:\Users\Administrator\Desktop\apk数据\2017-9-1
    if not os.path.exists(fullzipfilepath):
        print("Dir %s is not exists,input fullzipfilepaht")
        fullzipfilepath = raw_input()
    if not os.path.exists(unzipdir):
        os.mkdir(unzipdir)
    zf = zipfile.ZipFile(fullzipfilepath,'r')  #读方式打开压缩
    for filename in zf.namelist():  #zf.namelist() 获取压缩包文件中的文件列表
        eachfilepath = os.path.normpath(os.path.join(unzipdir,filename))  #将文件路径转化为正常路径，
                                                             # 从压缩文件获取的文件列表中，获取的文件格式是test1/2017-9-1.txt,
                                                             #无法创建目录或文件
        eachfiledir = os.path.dirname(eachfilepath)
        if not os.path.exists(eachfiledir):
            os.mkdir(eachfiledir)
            # os.makedirs(eachfiledir)  #使用makedirs(),递归创建目录,使用mkdir(),上级目录不存在,会报出异常
        fp = open(eachfilepath,'w')
        fp.write(str(zf.read(filename)))
        fp.close()
    zf.close()


if __name__ == '__main__':
    inputfile_path = "C:\\Users\\Administrator\\Desktop\\flask-chs.zip"
    # print_file(inputfile_path)
    
    # 压缩目录
    dirname = "C:\\Users\\Administrator\\Desktop\\2017-9-1"
    zipname = "2017-9-1.zip"
    zip_dir(dirname, zipname)
    
    # 解压文件
    zipfilename = "C:\\Users\\Administrator\\Desktop\\apk数据\\2017-9-1.zip"
    unzip_dir(zipfilename)