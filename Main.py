from UI.MainWindow import Ui_MainWindow
from UI.Setup_Field import UI_Setup_Field
from UI.Setup_Language import UI_Setup_Language
from UI.Test_List import Ui_Test_List
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

MAINWINDOW = None
SL = None
SF = None
TL = None

class Main(QMainWindow):
    def __init__(self) -> None:
        global MAINWINDOW, SL, TL, SF
        super().__init__()
        MAINWINDOW = Ui_MainWindow()
        self._set_slot()
        MAINWINDOW.show()

    def _set_slot(self):
        MAINWINDOW.actionLanguage.triggered.connect(self._sl_ui)
        MAINWINDOW.actionField.triggered.connect(self._sf_ui)
        MAINWINDOW.actionTest_List.triggered.connect(self._tl_ui)

    def _sl_ui(self):
        SL = UI_Setup_Language()
        SL.setupUi_Language()
        SL.show()

    def _sf_ui(self):
        SF = UI_Setup_Field()
        SF.setupUi_Field()
        SF.show()
        
    def _tl_ui(self):
        TL = Ui_Test_List()
        TL.setupUi_Test()
        TL.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Main()
    app.exec_()