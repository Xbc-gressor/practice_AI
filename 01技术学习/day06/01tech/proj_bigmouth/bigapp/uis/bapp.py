from PyQt5.QtWidgets import QApplication
import sys
from bigapp.uis.bdialog import BDialog

class BApp(QApplication):
    def __init__(self):
        super(BApp, self).__init__(sys.argv)
        # 构建QApplication与QDialog的关系：包含
        self.dlg = BDialog()
        self.dlg.show()
    