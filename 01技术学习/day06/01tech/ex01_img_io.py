"""
retval	=	cv.imread(	filename[, flags]	)
retval	=	cv.imwrite(	filename, img[, params]	)
"""

import cv2

img = cv2.imread("00016.png", cv2.IMREAD_COLOR) #IMREAD_GRAYSCALE)  # 读取后的格式很多，但是建议使用默认的读取方式
print(type(img))
print(img.shape)

cv2.imwrite("dd.png", img)