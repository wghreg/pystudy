#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/27 0027 下午 17:14
import gzip
import os

'''
    由于gz一般只压缩一个文件，所有常与其他打包工具一起工作。比如可以先用tar打包为XXX.tar,然后在压缩为XXX.tar.gz
    解压gz，其实就是读出其中的单一文件
'''
def un_gz(file_name):
    """ungz zip file"""
    # 获取文件的名称，去掉
    f_name = file_name.replace(".gz", "")
    # 创建gzip对象
    g_file = gzip.GzipFile(file_name)
    # gzip对象用read()打开后，写入open()建立的文件中。
    open(f_name, "w+").write(g_file.read())
    # 关闭gzip对象
    g_file.close()
