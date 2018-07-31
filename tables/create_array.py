#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# Date: 2018/7/30 0030 下午 15:28
import numpy as np
import tables

features = np.random.rand(100, 100000)
f = tables.openFile("feat.h5", 'w')
f.createArray(f.root, 'feature', features)
f.close()