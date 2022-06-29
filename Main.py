from UI.MainWindow import Ui_MainWindow
from UI.Setup_Language import UI_Setup_Language
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,\
     QPushButton, QVBoxLayout, QGraphicsScene, QCheckBox, QLabel, QWidget
import sys

class Main(QMainWindow, Ui_MainWindow, UI_Setup_Language):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.Form = QWidget()
        self.setupUi_Language(self.Form)
        self.set_slot()

    def set_slot(self):
        self.actionLanguage.triggered.connect(self.sl_ui)

    def sl_ui(self):
        self.setupUi_Language(self.Form)
        self.Form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = Main() 
    myWindow.show() 
    app.exec_()