import numpy
import cv2
"""
class numpy.ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None)
    shape : 数组形状
    dtype : 数组元素的类型
        图像数组： 1，3，4通道，每个元素类型：0-255：unsigned int8 = uint8
"""
# 构建数组 （图像 = 通道数：1，3，4）
img = numpy.ndarray(shape=(500, 500, 3), dtype=numpy.uint8)
img.fill(128)
cv2.imwrite("d2.png", img)
