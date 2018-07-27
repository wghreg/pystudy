#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/27 0027 下午 17:18

import os
import tarfile
'''
    XXX.tar.gz解压后得到XXX.tar，还要进一步解压出来。
    *注：tgz与tar.gz是相同的格式，老版本DOS扩展名最多三个字符，故用tgz表示。
    由于这里有多个文件，我们先读取所有文件名，然后解压
'''
def un_tar(file_name):
    """untar zip file"""
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    #由于解压后是许多文件，预先建立同名文件夹
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()