from PySide6.QtWidgets import QMainWindow
from ui import avt_win



class AuthWindows(avt_win.Ui_MainWindow,QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gest)

    def gest (self):
        from windows.gest2_win import GostWindows
        self.gest_win = GostWindows()
        self.gest_win.show()


    
