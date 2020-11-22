from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QDialog, QLabel
import sys

# 创建对象
"""
    PyQt5是包路径
    QtWidget 是模块，不是python模块，但是是C写的扩展名是pyd的dll模块
"""
app = QtWidgets.QApplication([]) # 传递命令行参数

# ---------------
# 创建窗体，处理事件
dlg = QDialog()
dlg.resize(300, 400)
button = QPushButton("确定");
button.setParent(dlg);
button.move(100, 100)

label = QLabel("这是一首简单的小情歌")
label.setParent(dlg)
label.move(50, 200)
dlg.show()
# ----------------

status = app.exec()

sys.exit(status)