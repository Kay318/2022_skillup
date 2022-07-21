from regex import E
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
        SF = UI_Setup_Field(MAINWINDOW)
        TL = Ui_Test_List(MAINWINDOW)
        self._set_slot()
        MAINWINDOW.show()

    def _set_slot(self):
        MAINWINDOW.actionLanguage.triggered.connect(self._sl_ui)
        MAINWINDOW.actionField.triggered.connect(self._sf_ui)
        MAINWINDOW.actionTest_List.triggered.connect(self._tl_ui)

    def _sl_ui(self):
        SL = UI_Setup_Language(MAINWINDOW)
        SL.setupUi_Language()
        MAINWINDOW.setDisabled(True)
        SL.show()

    def _sf_ui(self):
        SF.setupUi_Field()
        MAINWINDOW.setDisabled(True)
        SF.show()
        
    def _tl_ui(self):
        TL.setupUi_Test()
        MAINWINDOW.setDisabled(True)
        TL.setTest_Button()
        TL.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Main()
    app.exec_()