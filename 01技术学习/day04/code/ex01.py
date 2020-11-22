import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui
import sys

# 创建对象
"""
    PyQt5是包路径
    QtWidget 是模块，不是python模块，但是是C写的扩展名是pyd的dll模块
"""
app = PyQt5.QtWidgets.QApplication([]) # 传递命令行参数

# ---------------
# 创建窗体，处理事件
dlg = PyQt5.QtWidgets.QDialog()
dlg.show()
# ----------------

status = app.exec()

sys.exit(status)