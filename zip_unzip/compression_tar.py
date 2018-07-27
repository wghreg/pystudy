#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/27 0027 下午 17:24

# !/usr/bin/env /usr/local/bin/python
# encoding: utf-8
import tarfile
import os
from datetime import time
'''
    在写打包代码的过程中，使用tar.add()增加文件时，会把文件本身的路径也加进去，
    加上arcname就能根据自己的命名规则将文件加入tar包
'''
start = time.time()
tar = tarfile.open('/path/to/your.tar', 'w')
for root, dir, files in os.walk('/path/to/dir/'):
    for file in files:
        fullpath = os.path.join(root, file)
        tar.add(fullpath, arcname=file)
tar.close()
print(time.time() - start)

'''tar解包也可以根据不同压缩格式来解压'''
start = time.time()
t = tarfile.open("/path/to/your.tar", "r:")
t.extractall(path = '/path/to/extractdir/')
t.close()
print(time.time()-start)