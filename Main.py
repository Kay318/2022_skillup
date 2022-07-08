from UI.MainWindow import Ui_MainWindow
from UI.Setup_Language import UI_Setup_Language
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.mainWindow = Ui_MainWindow()
        self.sl = UI_Setup_Language()
        self.set_slot()

    def set_slot(self):
        self.mainWindow.actionLanguage.triggered.connect(self.sl_ui)

    def sl_ui(self):
        self.sl.setupUi_Language()
        self.sl.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = Main()
    app.exec_()