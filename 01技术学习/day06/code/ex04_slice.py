import numpy
import cv2
"""
支持的图像：bmp/jpg/png/gif/tiff
"""
img = cv2.imread("00016.png")

# print(img[1])  # 取一行
# print(img[1, 1])  # 某行某列的一个像素
# print(img[1, 1, 1]) # 取某个像素的颜色通道（分量）

# img[100] = 255
# img[100, 100] = [0, 0, 255]
# img[slice(50), slice(50,100, 3)] = 255
# img[50:100, 50:100:3, 0] = 255
# img[:,:,0] = 0

# print(img > 100)

print(img[:,:,0:1]>100)
img [img[:,:,:] > 100] = 0 

cv2.imwrite("d4.png", img)

