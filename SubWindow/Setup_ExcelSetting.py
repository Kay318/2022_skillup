import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))
from Helper import *
from Log import LogManager
from Settings import Setup as sp
# from MainWindow import MainWindow as mainwindow

class Setup_ExcelSetting(QDialog):
    signal = pyqtSignal(list, list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fieldList = parent.fieldList
        self.sp = sp.Settings()
        self.setupUI_Excel_Setting()

    @AutomationFunctionDecorator
    def setupUI_Excel_Setting(self):
        self.setWindowTitle("엑셀 설정")

        # 전체 화면 배치
        self.verticalLayout = QVBoxLayout(self)

        # 초기화 버튼
        self.reset_horizontalLayout = QHBoxLayout()
        self.null_text = QLabel("", self)
        self.reset_Button = QPushButton("초기화", self)
        self.reset_horizontalLayout.addWidget(self.null_text)
        self.reset_horizontalLayout.addWidget(self.reset_Button)
        self.verticalLayout.addLayout(self.reset_horizontalLayout)

        # Setup.ini 파일에 데이터를 창에 표시
        dataList, _ = self.sp.read_setup(table = "Excel_Setting")
        print(f'dataList : {dataList}')
        check_first = True
        self.start_settings = ["이미지 가로 크기", "이미지 세로 크기", "이미지 셀 행 크기", "시트 셀 기본 열 크기", "시트 셀 기본 행 크기"]
        self.start_settings_val = [400, 155, 115, 50, 15]

        for i in range(5):
            globals()[f'horizontalLayout{i}'] = QHBoxLayout()

            globals()[f'label{i}'] = QLabel()
            globals()[f'label{i}'].setText(f"{self.start_settings[i]}")
            globals()[f'horizontalLayout{i}'].addWidget(globals()[f'label{i}'])

            globals()[f'lineEdit{i}'] = QLineEdit()
            globals()[f'horizontalLayout{i}'].addWidget(globals()[f'lineEdit{i}'])
            self.verticalLayout.addLayout(globals()[f'horizontalLayout{i}'])
            try:
                globals()[f'lineEdit{i}'].setText(dataList[i])
            except:
                pass

            # 포커스 설정: 빈칸 혹은 마지막칸
            if (globals()[f'lineEdit{i}'].text() == "" or i==7) and check_first:
                globals()[f'lineEdit{i}'].setFocus()
                check_first = False

        # [확인], [취소] 버튼
        self.ok_horizontalLayout = QHBoxLayout()
        self.ok_horizontalLayout.setAlignment(Qt.AlignRight)
        
        self.ok_Button = QPushButton("확인", self)
        self.ok_horizontalLayout.addWidget(self.ok_Button)
        self.cancel_Button = QPushButton("취소", self)
        self.ok_horizontalLayout.addWidget(self.cancel_Button)
        self.verticalLayout.addLayout(self.ok_horizontalLayout)

        # 버튼 이벤트 함수
        self.tl_set_slot()

        self.tl_ini_set()

    @AutomationFunctionDecorator
    def tl_set_slot(self):
        self.reset_Button.clicked.connect(self.reset_Button_clicked)
        self.ok_Button.clicked.connect(self.ok_Button_clicked)
        self.cancel_Button.clicked.connect(self.close)

    @AutomationFunctionDecorator
    def tl_ini_set(self):

        start_set = False
        for i in range(5):
            if globals()[f'lineEdit{i}'].text() == "":
                start_set = True
            else:
                start_set = False
                break
        
        if start_set:
            for i in range(5):
                globals()[f'lineEdit{i}'].setText(str(self.start_settings_val[i]))
            
            self.excel_ini_set()

    @AutomationFunctionDecorator
    def excel_ini_set(self):
        start_settings = ["이미지 가로 크기", "이미지 세로 크기", "이미지 셀 행 크기", "시트 셀 기본 열 크기", "시트 셀 기본 행 크기"]
        start_settings_val = [400, 155, 115, 50, 15]

        for i in range(5):
            self.sp.write_setup(table="Excel_Setting", count=None, val=start_settings[i], val2=start_settings_val[i])
        self.sp.save_ini()

    @AutomationFunctionDecorator
    def reset_Button_clicked(self, litter):
        LogManager.HLOG.info("엑셀 설정 팝업 확인 버튼 선택")
        reply = QMessageBox.question(self, '알림', '초기화 하시겠습니까?',
                                    QMessageBox.Ok | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Ok:
            LogManager.HLOG.info("엑셀 설정 초기화 선택")
            for i in range(5):
                globals()[f'lineEdit{i}'].setText(str(self.start_settings_val[i]))

        else:
            LogManager.HLOG.info("엑셀 설정 초기화 취소 선택")

    @AutomationFunctionDecorator
    def ok_Button_clicked(self, litter):
        LogManager.HLOG.info("엑셀 설정 팝업 확인 버튼 선택")
        testList = []
        testCheck = False

        # 중복 체크
        for i in range(5):
            if globals()[f'lineEdit{i}'].text() != "":

                text = globals()[f'label{i}'].text()
                intBool = False
                try:
                    int(globals()[f'lineEdit{i}'].text())
                    intBool = True
                except:
                    QMessageBox.warning(self, '주의', f'{text} 수치를 숫자형태로 지정해주세요.')
                    intBool = False
                    return

                if (intBool):
                    if 0 > int(globals()[f'lineEdit{0}'].text()) or int(globals()[f'lineEdit{0}'].text()) > 999:
                        text = globals()[f'label{0}'].text()
                        QMessageBox.warning(self, '주의', f'{text} 0에서 1000자 사이여야 합니다.')
                        testCheck = False
                        return
                    elif 0 > int(globals()[f'lineEdit{1}'].text()) or int(globals()[f'lineEdit{1}'].text()) > 999:
                        text = globals()[f'label{1}'].text()
                        QMessageBox.warning(self, '주의', f'{text} 0에서 1000자 사이여야 합니다.')
                        testCheck = False
                        return
                    elif 0 > int(globals()[f'lineEdit{2}'].text()) or int(globals()[f'lineEdit{2}'].text()) > 409:
                        QMessageBox.warning(self, '주의', '엑셀 이미지 행 너비는 0에서 409자 사이여야 합니다.')
                        testCheck = False
                        return
                    elif 0 > int(globals()[f'lineEdit{3}'].text()) or int(globals()[f'lineEdit{3}'].text()) > 255:
                        QMessageBox.warning(self, '주의', '엑셀 열 너비는 0에서 255자 사이여야 합니다.')
                        LogManager.HLOG.info(f'엑셀설정 팝업에서 엑셀 열 크기 제한 알림 표시')
                        testCheck = False
                        return
                    elif 0 > int(globals()[f'lineEdit{4}'].text()) or int(globals()[f'lineEdit{4}'].text()) > 409:
                        QMessageBox.warning(self, '주의', '엑셀 행 너비는 0에서 409자 사이여야 합니다.')
                        LogManager.HLOG.info(f'엑셀설정 팝업에서 엑셀 행 너비 제한 알림 표시')
                        testCheck = False
                        return
                    else:
                        testCheck = True
            else:
                text = globals()[f'label{i}'].text()
                QMessageBox.warning(self, '주의', f'{text} 수치가 비어있습니다.')
                return
        else:
            self.signal.emit([], [])
            self.destroy()

        if (testCheck):
            self.sp.config["Excel_Setting"] = {}
            for i in range(5):
                if globals()[f'lineEdit{i}'].text() != "":
                    self.sp.write_setup(table = "Excel_Setting", 
                                        count=None, 
                                        val=self.start_settings[i],
                                        val2=globals()[f'lineEdit{i}'].text())
                    LogManager.HLOG.info(f"{i+1}:평가 목록 팝업에 {globals()[f'lineEdit{i}'].text()} 추가")
            if testList == []:
                testList = ["OK"]
                self.sp.clear_table("Excel_Setting")
            self.destroy()

    def check_changedData(self):
        """변경사항이 있는지 체크하는 함수

        Returns:
            _type_: 변경사항이 있으면 True, 없으면 False
        """
        setupList, _ = self.sp.read_setup("Excel_Setting")
        lineList = [globals()[f'lineEdit{i}'].text() for i in range(5) if globals()[f'lineEdit{i}'].text() != ""]
        
        if setupList != lineList:
            return True
        else:
            return False
        
    @AutomationFunctionDecorator
    def closeEvent(self, event) -> None:
        LogManager.HLOG.info("엑셀 설정 팝업 취소 버튼 선택")

        if self.check_changedData():
            reply = QMessageBox.question(self, '알림', '변경사항이 있습니다.\n취소하시겠습니까?',
                                    QMessageBox.Ok | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Ok:
                LogManager.HLOG.info("필드 설정 팝업 > 취소 > 변경사항 알림에서 예 선택")
                event.accept()
                self.signal.emit([], [])
            else:
                LogManager.HLOG.info("필드 설정 팝업 > 취소 > 변경사항 알림에서 취소 선택")
                event.ignore()
        else:
            self.signal.emit([], [])
            # mainwindow.setEnabled(True)
            self.destroy()

                
    @AutomationFunctionDecorator
    def keyPressEvent(self, a0: QKeyEvent) -> None:
        
        KEY_ENTER = 16777220
        KEY_SUB_ENTER = 16777221
        KEY_CLOSE = 16777216

        if a0.key() == KEY_ENTER or a0.key() == KEY_SUB_ENTER:
            self.ok_Button_clicked(None)
        elif a0.key() == KEY_CLOSE:
            self.close()

if __name__ == "__main__":
    LogManager.Init()
    app = QApplication(sys.argv)
    ui = Setup_ExcelSetting()
    ui.show()
    sys.exit(app.exec_())