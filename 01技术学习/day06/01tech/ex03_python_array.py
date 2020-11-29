import numpy
import cv2

arr = [[[x*2%256, y*2%256, (x+y)%256] for x in range(500)] for y in range(500)]

img = numpy.array(arr)  # 把python的list转换为ndarray

cv2.imwrite("dd.png", img)

