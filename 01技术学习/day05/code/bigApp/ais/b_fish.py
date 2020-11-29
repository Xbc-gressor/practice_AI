from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPen, QColor


class BFish(QThread):
    signal_open = pyqtSignal()
    
    def __init__(self):
        super(BFish, self).__init__()
        # 信号
        self.x = 100
        self.y = 100
        self.size = 200
        self.dir = 45
        self.speed = 2
        self.is_open = False
        self.m = 45

    def run(self):
        # run结束线程死亡
        while True:
            self.signal_open.emit()
            self.open_mouth()
            QThread.usleep(10000)

    # 根据方向进行移动
    def swim(self):
        if(self.dir == 0):
            self.x += self.speed
        elif(self.dir == 90):
            self.y -= self.speed
        elif(self.dir == 180):
            self.x -= self.speed
        elif(self.dir == 270):
            self.y += self.speed

    def change_dir(self, dir):
        self.dir = dir

    def open_mouth(self):
        if self.is_open:
            self.m += 1
            if self.m >= 45:
                self.is_open = not self.is_open
                self.m = 45
        else:
            self.m -= 1
            if self.m <= 0:
                self.is_open = not self.is_open
                self.m = 0

    def show_me(self, g):
        # 颜色
        color = QColor(12,32,123)
        pen = QPen(color, 4.0, Qt.DashDotDotLine)
        g.setPen(pen)
        # 绘制图形
        g.drawPie(
            self.x, self.y,
            self.size, self.size,
            (self.m + self.dir) * 16,
            (360 - 2 * self.m) * 16
        )

    