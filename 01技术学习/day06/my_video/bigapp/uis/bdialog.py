from PyQt5.QtWidgets import QDialog
from bigapp.uis.videoui import Ui_Video
from bigapp.uis.bvideo import BVideoTh
from PyQt5.QtGui import QImage, QPixmap

class BDialog(QDialog):
    def __init__(self):
        super(BDialog, self).__init__()
        # 将设计的ui界面加载到窗体中
        self.ui = Ui_Video()
        self.ui.setupUi(self)

        # 启动摄像任务
        self.th = BVideoTh()
        # 绑定信号与槽
        self.th.signal_video.connect(self.show_video)
        self.th.start()

    def show_video(self, h, w, c, data):
        # print("有图像发送", h, w, c)
        # 构造QImage
        qimg = QImage(data, w, h, w*c, QImage.Format_RGB888)
        # 转换成QPixmap
        qpixmap = QPixmap.fromImage(qimg)
        # 设置到标签
        self.ui.lbl_video.setPixmap(qpixmap)
            # 设置视频缩放来适合标签框大小
        self.ui.lbl_video.setScaledContents(True)
