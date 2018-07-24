#! /usr/bin/env python3
# *-* coding:utf-8 *-*

'''PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。

安装Pillow
如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：

$ pip install pillow
如果遇到Permission denied安装失败，请加上sudo重试。'''

from PIL import Image, ImageFilter

im = Image.open("D://test.png")
# 获取图像尺寸
w, h = im.size

print("image size: %s x %s" % (w, h))

# 缩放到50%
im.thumbnail((w//2, h//2))
print("resize image to : %s x %s" % (w//2, h//2))
# 把缩放后的图片用jpeg保存
# 图片模式不对，需要转换
im = im.convert('RGB')
im.save("D://thumbnail.jpg", 'jpeg')

# 模糊效果
im2 = im.filter(ImageFilter.BLUR);
im2.save('D://blur.png', 'png')



