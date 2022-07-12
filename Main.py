from UI.MainWindow import Ui_MainWindow
from UI.Setup_Language import UI_Setup_Language
from UI.Test_List import Ui_Test_List
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

MAINWINDOW = None
SL = None
TL = None

class Main(QMainWindow):
    def __init__(self) -> None:
        global MAINWINDOW, SL, TL
        super().__init__()
        MAINWINDOW = Ui_MainWindow()
        SL = UI_Setup_Language()
        TL = Ui_Test_List()
        self.set_slot()

    def set_slot(self):
        MAINWINDOW.actionLanguage.triggered.connect(self.sl_ui)
        MAINWINDOW.actionTest_List.triggered.connect(self.tl_ui)

    def sl_ui(self):
        SL.setupUi_Language()
        SL.show()
        
    def tl_ui(self):
        TL.setupUi_Test()
        TL.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = Main()
    app.exec_()