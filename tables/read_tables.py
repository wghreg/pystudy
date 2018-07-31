#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# Date: 2018/7/30 0030 下午 15:27

from tables import *

# 读取数据
f = open_file("tutorial.h5", mode='r', title='test file')
table = f.root.detector.readout
energy = []
for x in table.iterrows():
    energy.append(x)

print(energy)