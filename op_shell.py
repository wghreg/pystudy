#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# Date: 2018/7/31 0031 下午 17:30

import subprocess
'''
 Python和Shell的交互，可以通过subprocess这个内置模块实现，它能帮助我们直接执行Shell命令，并且获取返回的结果。
 模块还支持控制Shell进程的输入输出等... 但如果是比较复杂的Shell脚本，还是推荐直接用Shell编写，然后Python调用实现起来更加方便
'''
date = subprocess.getstatusoutput('date')
time = subprocess.getstatusoutput('time')
print(date, time)