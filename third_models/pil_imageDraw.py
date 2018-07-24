#! /usr/bin/env python3
# *-* coding:utf-8 *-*

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色
def rndColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def rndColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

width = 240
height = 50
# 生成图片
image = Image.new('RGB', (width, height), (255,255,255))
# 字体
font = ImageFont.truetype('C:\\Windows\\Fonts\\arial.ttf', 36)

# 画图
draw = ImageDraw.Draw(image)

# 填充像素
for x in range(width):
    for y in range(height):
        draw.point((x,y), rndColor())

# 输出文字
for t in range(4):
    draw.text((60*t+10, 10), rndChar(), font, rndColor2())

image.savez("d://gen_code.jpg", 'jpeg')
image = image.filter(ImageFilter.BLUR)
image.save('D://code.jpg', 'jpeg')