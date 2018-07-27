#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/27 0027 下午 17:20
import rarfile
import os
'''
    因为rar通常为window下使用，需要额外的Python包rarfile。
    可用地址： http://sourceforge.net/projects/rarfile.berlios/files/rarfile-2.4.tar.gz/download
    解压到Python安装目录的/Scripts/目录下，在当前窗口打开命令行,
    输入Python setup.py install
    安装完成。
'''
def un_rar(file_name):
    """unrar zip file"""
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    
    os.chdir(file_name + "_files")
        
    rar.extractall()
    rar.close()