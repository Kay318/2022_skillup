from regex import E
from UI.MainWindow import Ui_MainWindow
from UI.Setup_Field import UI_Setup_Field
from UI.Setup_Language import UI_Setup_Language
from UI.Test_List import Ui_Test_List
from UI.excel_create import Ui_excel_create
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

MAINWINDOW = None
SL = None
SF = None
TL = None
EC = None

class Main(QMainWindow):
    def __init__(self) -> None:
        global MAINWINDOW, SL, TL, SF, EC
        super().__init__()
        MAINWINDOW = Ui_MainWindow()
        SL = UI_Setup_Language(MAINWINDOW)
        SF = UI_Setup_Field(MAINWINDOW)
        TL = Ui_Test_List(MAINWINDOW)
        EC = Ui_excel_create(MAINWINDOW)
        self._set_slot()
        self.wigets_setupUi()
        MAINWINDOW.show()

    def _set_slot(self):
        MAINWINDOW.actionLanguage.triggered.connect(self._sl_ui)
        MAINWINDOW.actionField.triggered.connect(self._sf_ui)
        MAINWINDOW.actionTest_List.triggered.connect(self._tl_ui)
        MAINWINDOW.actionCreateExcel.triggered.connect(self._excel_setiing_show)

    # 0726
    def wigets_setupUi(self):
        SL.setupUi_Language()
        EC.setupUi()
        SF.setupUi_Field()
        TL.setupUi_Test()

    def _sl_ui(self):
        MAINWINDOW.setDisabled(True)
        SL.show()

    def _sf_ui(self):
        MAINWINDOW.setDisabled(True)
        SF.show()
        
    def _tl_ui(self):
        MAINWINDOW.setDisabled(True)
        TL.setTest_Button()
        TL.show()       

    def _excel_setiing_show(self):
        MAINWINDOW.setDisabled(True)
        EC.langSetting()
        EC.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Main()
    app.exec_()