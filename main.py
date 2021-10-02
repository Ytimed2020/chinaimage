import cv2
from PIL import Image
import numpy as np
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt



def china_image(src):
    flag = Image.open('china.png')  # 读入国旗图像
    w, h = src.size  # 获取图像尺寸
    mask = flag.resize((w, h))  # 将国旗重置为图像尺寸
    # 将国旗图像处理为掩膜
    for i in range(w):
        for j in range(h):
            pixel = mask.getpixel((i, j))  # RGB颜色值
            alpha = 255 - i // 2  # 调整透明度，越往右透明度越低的意思
            if alpha < 0:
                alpha = 0
            pixel = pixel[:-1] + (alpha,)  # 跑去最后一行变成透明度
            mask.putpixel((i, j), pixel)  # 将掩膜粘贴到图像中
    src.paste(mask, (0, 0), mask)
    return src


if __name__ == "__main__":
    src_image = Image.open('cat.jpg')
    save_image = china_image(src_image)  # 保存图像至相应位置
    save_image.save('new_image.png')
