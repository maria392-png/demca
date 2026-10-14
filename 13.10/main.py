from PySide6.QtWidgets import QApplication
from windows.avt2_win import AuthWindows

app = QApplication([])
avt2_win = AuthWindows()
avt2_win.show()

app.exec()