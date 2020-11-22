from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtCore import Qt

class WDialog(QDialog):

    def __init__(self):
        super(WDialog, self).__init__()
        self.resize(300, 400)
        self.btn = QPushButton("hahahahaha", self)


    def closeEvent(self, event):
        print("窗体关闭")

    def keyPressEvent(self, event):
        print("按键", event.modifiers()==Qt.ShiftModifier, "+", event.text()) # , event.key()
  
