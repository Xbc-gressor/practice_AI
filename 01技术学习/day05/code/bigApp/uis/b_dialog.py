from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPainter
from bigApp.ais.b_fish import BFish
from PyQt5.QtCore import Qt

class BDialog(QDialog):
    def __init__(self):
        super(BDialog, self).__init__()
        self.fish = BFish()
        self.fish.start()
        self.fish.signal_open.connect(self.repaint)

    # 控制鱼的方向
    def keyPressEvent(self, a0):
        # 键盘的按键处理 👆 👇 👈 👉
        key = a0.key()
        if key == Qt.Key_Right:
            self.fish.change_dir(0)
            self.fish.swim()
        elif key == Qt.Key_Up:
            self.fish.change_dir(90)
            self.fish.swim()
        elif key == Qt.Key_Left:
            self.fish.change_dir(180)
            self.fish.swim()
        elif key == Qt.Key_Down:
            self.fish.change_dir(270)
            self.fish.swim()


    def paintEvent(self, a0):
        #print("窗口在绘制")
        painter = QPainter(self)
        # painter.drawPie(100, 100, 200, 200, 45*16, (360-2*45)*16)
        self.fish.show_me(painter)
