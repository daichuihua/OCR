'''
tesseract 安装及使用教程的网址：
https://blog.csdn.net/showgea/article/details/82656515
OCR的难点问题:复杂背景、艺术字体、低分辨率、非均匀光照、图像退化、字符形变、多语言混合、文本行复杂版式、检测框字符残缺
测试效果：对于背景比较单纯的英文字符的识别效果还不错，但对中文字符和背景比较复杂的情况，识别效果不理想
步骤：
1、安装tesseract程序
2、修改程序中tesseract执行程序的位置
3、修改原图SRC_PATH的位置
4、执行程序
'''
# pylint --disable=F0401 <filename>
# -*- coding: UTF-8 -*-

from PIL import Image
import numpy as np
import pytesseract
import cv2

# path of pytesseract execution folder
pytesseract.pytesseract.tesseract_cmd = 'D:\\OCR V5\\tesseract.exe'
# Path of image
SRC_PATH = 'OCR_08.png'

"""文字识别函数"""
def get_string(pic_path):
    """get_string function used for getting string from the picture"""
    # Reading picture with opencv
    pic = cv2.imread(pic_path)

    # grey-scale the picture
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    # Do dilation and erosion to eliminate unwanted noises
    kernel = np.ones((1, 1), np.uint8)
    pic = cv2.dilate(pic, kernel, iterations=20)
    pic = cv2.erode(pic, kernel, iterations=20)

    # Write image after removed noise
    cv2.imwrite(pic_path + "no_noise.png", pic)

    #  threshold applying to get only black and white picture
    pic = cv2.adaptiveThreshold(pic, 300, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image for later recognition process
    cv2.imwrite(pic_path + "threshold.png", pic)

    # Character recognition with tesseract
    final = pytesseract.image_to_string(Image.open(pic_path + "threshold.png"))

    return final

#starts recognition of characters
print(get_string(SRC_PATH))
#displays the output when it recognizes
