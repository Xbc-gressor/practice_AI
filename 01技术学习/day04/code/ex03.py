from UIs.wapplication import WApplication
from UIs.wdialog import WDialog
import sys

sys.path.append("UIs")

app = WApplication()
dlg = WDialog()
dlg.show()
app.exec()