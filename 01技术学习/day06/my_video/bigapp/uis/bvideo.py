"""
    使用多线程和cv库实现摄像头连接
"""
import numpy
from PyQt5.QtCore import QThread, pyqtSignal
import cv2


class BVideoTh(QThread):
    # 创建信号对象
    signal_video = pyqtSignal(int, int, int, bytes)

    def __init__(self):
        super(BVideoTh, self).__init__()
        # 创建摄像头对象
        self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def run(self):
        while True:
            # 状态   图像    实现抓取视频
            status, frame = self.dev.read()
            if status:
                # print(frame.shape)
                h, w, c = frame.shape
                # 做一个图像处理
                # frame[100:200, :, 0] = 0
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 进行卷积处理
                frame = self.filter(frame)
                self.signal_video.emit(h, w, c, frame.tobytes())
            else:
                print("设备故障！")
                break  # 结束线程
            QThread.usleep(100000)

    """卷积处理"""
    @staticmethod
    def filter(img):
        # kernel = numpy.array([
        #     [-1, 0, 1],
        #     [-1, 0, 1],
        #     [-1, 0, 1]
        # ])
        # return cv2.filter2D(img, -1, kernel, delta=128)
        # return cv2.GaussianBlur(img, ksize=(11, 11), sigmaX=5)
        return cv2.Sobel(img, ddepth=-1, dx=2, dy=2, ksize=7, delta=50)
