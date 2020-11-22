from PyQt5.QtWidgets import QApplication
import sys

class WApplication(QApplication):
    def __init__(self):
        super(WApplication, self).__init__(sys.argv)
        # 添加自己的数据
