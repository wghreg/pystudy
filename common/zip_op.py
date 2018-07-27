#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/27 0027 上午 11:45

import os
import zipfile
from zipfile import ZipFile

def print_file(inputfile_path):
    myzip = ZipFile(inputfile_path, 'r')
    for file_name in myzip.namelist():
        for data in myzip.open(file_name, 'r'):
            print(data)
    myzip.close()

if __name__ == '__main__':
    inputfile_path = "C:\\Users\\Administrator\\Desktop\\flask-chs.zip"
    # print_file(inputfile_path)

# 压缩目录
def zip_dir(dirname, zipfilename):
    filelist = []
    # 判断压缩目录是否文件，是则添加到文件列表中
    if os.path.isfile(dirname):
        filelist.append(dirname)
