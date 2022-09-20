from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from Log import LogManager
from Screen import *
from Helper import *

MAINWINDOW = None
SL = None
SF = None
TL = None
CE = None
    
class Main(QMainWindow):
    def __init__(self) -> None:
        global MAINWINDOW, SL, TL, SF, CE
        super().__init__()
        MAINWINDOW = MainWindow()
        SL = UI_Setup_Language(MAINWINDOW)
        SF = UI_Setup_Field(MAINWINDOW)
        TL = UI_TestList(MAINWINDOW)
        CE = UI_CreateExcel(MAINWINDOW)
        self.__set_slot()
        self.__wigets_setupUi()
        MAINWINDOW.show()

    @AutomationFunctionDecorator
    def __set_slot(self):
        MAINWINDOW.actionLanguage.triggered.connect(self.__sl_ui)
        MAINWINDOW.actionField.triggered.connect(self.__sf_ui)
        MAINWINDOW.actionTest_List.triggered.connect(self.__tl_ui)
        MAINWINDOW.actionCreateExcel.triggered.connect(self.__ce_ui)

    # 0726
    @AutomationFunctionDecorator
    def __wigets_setupUi(self):
        SL.setupUI_Language()
        CE.setupUI_CreateExcel()
        SF.setupUI_Field()
        TL.setupUI_TestList()

    @AutomationFunctionDecorator
    def __sl_ui(self):
        MAINWINDOW.setDisabled(True)
        SL.setLang_Button() # 0728
        SL.show()

    @AutomationFunctionDecorator
    def __sf_ui(self):
        MAINWINDOW.setDisabled(True)
        SF.show()
    
    @AutomationFunctionDecorator
    def __tl_ui(self):
        MAINWINDOW.setDisabled(True)
        TL.setTest_Button()
        TL.show()       

    @AutomationFunctionDecorator
    def __ce_ui(self):
        MAINWINDOW.setDisabled(True)
        CE.langSetting()
        CE.show()

def Init():
    LogManager.Init()

if __name__ == "__main__":
    Init()
    app = QApplication(sys.argv)
    myWindow = Main()
    app.exec_()