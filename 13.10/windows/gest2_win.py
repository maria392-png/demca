from PySide6.QtWidgets import QMainWindow
from ui import gest_win2


class GostWindows(gest_win2.Ui_MainWindow,QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

