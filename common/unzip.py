#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# date: 2018/7/27 0027 下午 15:31

import zipfile

def unzip_to_txt_plus(zipfilename):
  zfile = zipfile.ZipFile(zipfilename, 'r')
  for filename in zfile.namelist():
    data = zfile.read(filename)
    # data = data.decode('gbk').encode('utf-8')
    data = data.decode('gbk', 'ignore').encode('utf-8')
    file = open(filename, 'w+b')
    file.write(data)
    file.close()


if __name__ == '__main__':
  zipfilename = "C:\\Users\\Administrator\\Desktop\\flask-chs.zip"
  unzip_to_txt_plus(zipfilename)

