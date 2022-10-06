from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from functools import partial
from Database.DB import DBManager
from Helper import *
from Settings import Setup as sp

class UI_TestList(QWidget, DBManager):
    def __init__(self, mainwindow):
        super().__init__()
        DBManager().__init__()
        
        self.key = []
        self.mainwin = mainwindow
        self.sp = sp.Settings()

    @AutomationFunctionDecorator
    def setupUI_TestList(self):

        self.sethorizontalLayout = QHBoxLayout(self)
        self.sethorizontalLayout.setObjectName("horizontalLayout")
        self.set_QWidget = QtWidgets.QWidget(self)
        self.set_QWidget.setObjectName("set_QWidget")
        self.addTest_Button = QtWidgets.QPushButton(self)
        self.addTest_Button.setObjectName("addTest_Button")
        self.ok_Button = QPushButton(self)
        self.ok_Button.setObjectName("set_ok_Button")
        self.cancel_Button = QPushButton(self)
        self.cancel_Button.setObjectName("set_cancel_Button")
        self.add_verticalLayout = QVBoxLayout(self)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_btn_QWidget = QtWidgets.QWidget(self)
        self.set_btn_QWidget = QtWidgets.QWidget(self)
        self.fill_verticalLayout = QVBoxLayout(self)

        self.TestList_scrollArea = QScrollArea(self)
        self.TestList_scrollAreaWidgetContents = QWidget()
        self.TestListScroll_verticalLayout = QVBoxLayout(self.TestList_scrollAreaWidgetContents)

        self.setObjectName("Form")
        self.resize(400, 400)
        self.addTest_Button.setGeometry(QtCore.QRect(150, 10, 101, 41))
        self.add_btn_QWidget.setGeometry(QtCore.QRect(150, 10, 101, 41))
        self.set_QWidget.setGeometry(QtCore.QRect(20, 70, 361, 241))
        self.set_btn_QWidget.setGeometry(QtCore.QRect(220, 317, 161, 41))
        self.ok_Button.setGeometry(QtCore.QRect(1, 3, 76, 23))
        self.cancel_Button.setGeometry(QtCore.QRect(83, 3, 76, 23))
        self.TestList_scrollAreaWidgetContents.setGeometry(QtCore.QRect(20, 70, 361, 241))

        self.addTest_Button.setText("평가 목록 추가")
        self.addTest_Button.setMinimumWidth(101)
        self.addTest_Button.setMinimumHeight(41)
        self.ok_Button.setText("확인")
        self.cancel_Button.setText("취소")
        self.add_verticalLayout.addWidget(self.addTest_Button)
        self.add_verticalLayout.setAlignment(Qt.AlignCenter)

        self.TestList_scrollArea.setWidgetResizable(True)
        self.TestListScroll_verticalLayout.setAlignment(Qt.AlignTop)

        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)

        # [확인], [취소] 버튼
        self.sethorizontalLayout.setAlignment(Qt.AlignRight)
        self.sethorizontalLayout.addWidget(self.ok_Button)
        self.sethorizontalLayout.addWidget(self.cancel_Button)

        self.add_btn_QWidget.setLayout(self.add_verticalLayout)
        self.set_QWidget.setLayout(self.verticalLayout)
        self.set_btn_QWidget.setLayout(self.sethorizontalLayout)

        # 버튼 이벤트 함수
        self.btn_set_slot()

        self.fill_verticalLayout.addWidget(self.add_btn_QWidget)
        self.fill_verticalLayout.addWidget(self.set_QWidget)
        self.fill_verticalLayout.addWidget(self.set_btn_QWidget)
        self.setLayout(self.fill_verticalLayout)

    @AutomationFunctionDecorator
    def btn_set_slot(self):
        self.addTest_Button.clicked.connect(partial(self.addTest_Button_clicked, val = "", litter = None)) # 0719
        self.ok_Button.clicked.connect(partial(self.ok_Button_clicked))
        self.cancel_Button.clicked.connect(partial(self.cancel_Button_clicked))

    @AutomationFunctionDecorator
    def setTest_Button(self):

        self.cnt = 0
        List = []
        # 중복제거 중간점검
        result_val, result_val2 = self.sp.read_ini__test(table = "Test_List")
        
        for i in result_val:
            List.append(i)

        if List != NULL and len(self.TestListScroll_verticalLayout) != 0:

            item_list = list(range(self.TestListScroll_verticalLayout.count()))
            item_list.reverse()#  Reverse delete , Avoid affecting the layout order 

            for i in item_list:

                try:
                    globals()[f'TestList_horizontalLayout{i}'].itemAt(0).widget().deleteLater() 
                    globals()[f'TestList_horizontalLayout{i}'].itemAt(1).widget().deleteLater() 
                except Exception as e:
                    continue

                item = self.TestListScroll_verticalLayout.itemAt(i)
                self.TestListScroll_verticalLayout.removeItem(item)
                if item.widget():
                    item.widget().deleteLater()

        for val in List:
            print(f'val {val}')
            self.addTest_Button_clicked(val= val, litter=None)
        
        self.setup_Button_lenght = self.verticalLayout.count()
        print(f"self.setup_Button_lenght : {self.setup_Button_lenght}")

    def addTest_Button_clicked(self, val, litter):

        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)

        globals()[f'TestList_horizontalLayout{self.cnt}'] = QHBoxLayout()

        # 삭제 버튼
        globals()[f'del_TestList_btn{self.cnt}'] = QPushButton("-", self.TestList_scrollAreaWidgetContents)
        globals()[f'del_TestList_btn{self.cnt}'].setMaximumWidth(30)
        globals()[f'del_TestList_btn{self.cnt}'].clicked.connect(partial(
            self.del_TestList_btn_clicked, layout = globals()[f'TestList_horizontalLayout{self.cnt}'], cnt = self.cnt))
        
        # 내용 입력
        globals()[f'Test_lineEdit{self.cnt}'] = QLineEdit(self.TestList_scrollAreaWidgetContents)
        globals()[f'Test_lineEdit{self.cnt}'].setMaximumWidth(300)
        
        if (val != None):

            globals()[f'Test_lineEdit{self.cnt}'].setText(val)
        else:
            globals()[f'Test_lineEdit{self.cnt}'].setText("")
            
            for val in range(self.cnt + 1):

                if globals()[f'Test_lineEdit{val}'].text() == "":
                    globals()[f'Test_lineEdit{val}'].setFocus()
                    break

        print(f"globals()[f'Test_lineEdit{self.cnt}'].text() : {globals()[f'Test_lineEdit{self.cnt}'].text()}")
            
        globals()[f'TestList_horizontalLayout{self.cnt}'].addWidget(globals()[f'del_TestList_btn{self.cnt}'])
        globals()[f'TestList_horizontalLayout{self.cnt}'].addWidget(globals()[f'Test_lineEdit{self.cnt}'])

        self.TestListScroll_verticalLayout.addLayout(globals()[f'TestList_horizontalLayout{self.cnt}'])

        self.cnt += 1
        
        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)

    # @AutomationFunctionDecorator
    def del_TestList_btn_clicked(self, layout, cnt):
        """라인 삭제 함수

        Args:
            cnt: 변수명
        """

        print(f'set_self.TestListScroll_verticalLayout.count() : {self.TestListScroll_verticalLayout.count()}')

        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

        item_list = list(range(self.TestListScroll_verticalLayout.count()))
        item_list.reverse()#  Reverse delete , Avoid affecting the layout order 

        for i in item_list:

            item = self.TestListScroll_verticalLayout.itemAt(i)

            if (layout == item):
                print("PASS")
                self.TestListScroll_verticalLayout.removeItem(item)

    @AutomationFunctionDecorator
    def ok_Button_clicked(self, litter):

        checkOverlap = []

        # 빈칸 및 중복 언어 체크
        for i in range(self.cnt):
            try:
                if (globals()[f'Test_lineEdit{i}'].text() == ""):
                    QMessageBox.about(self, '주의', '빈칸이 있습니다. \n 확인해 주세요.')
                    return
            except RuntimeError:
                continue

            if (globals()[f'Test_lineEdit{i}'].text() not in checkOverlap):
                checkOverlap.append(globals()[f'Test_lineEdit{i}'].text())
            else:
                QMessageBox.about(self, '주의', f'{i+1}번째 라인이 중복으로 입력되었습니다.')
                return

            if (len(globals()[f'Test_lineEdit{i}'].text()) > 15):
                QMessageBox.about(self, '주의', f'{i+1}번째 라인에서 15자 입력이 초과 하였습니다.')
                return

        # DB에 저장
        self.c.execute(f"DELETE FROM Test_List")
        self.sp.create_table(table="Test_List")
        if (self.TestListScroll_verticalLayout.count() != 0) :
            for i in range(self.cnt):
                try:
                    self.test = self.sp.with_ini_test(table = "Test_List", 
                        count=i, 
                        val=globals()[f'Test_lineEdit{i}'].text(),
                        val2=None)
                    self.dbConn.execute(f"INSERT INTO Test_List VALUES (?)", 
                            (globals()[f'Test_lineEdit{i}'].text(),))
                    
                except RuntimeError:
                    continue
        self.sp.save_ini(self.test) # 여기수정
        self.dbConn.commit()
    
        self.mainwin.setWidget_func()
        self.close()

    @AutomationFunctionDecorator
    def cancel_Button_clicked(self, litter):

        self.close()

    @AutomationFunctionDecorator
    def closeEvent(self, event) -> None:
        self.c.execute('SELECT * FROM Test_List')
        dataList = self.c.fetchall()
        temp_cnt = 1

        dbList = [data[0] for data in dataList]
        lineList = []
        for i in range(self.cnt):
            try:
                lineList.append(globals()[f'Test_lineEdit{i}'].text())
            except RuntimeError:
                continue

        if dbList != lineList:
            reply = QMessageBox.question(self, '알림', '변경사항이 있습니다.\n취소하시겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                for i in range(self.cnt):
                    globals()[f'Test_lineEdit{i}'].setText("")

                if len(dataList) > 0:
                    for data in dataList:
                        globals()[f'Test_lineEdit{temp_cnt-1}'].setText(data[0])
                        temp_cnt += 1
                event.accept()
            else:
                event.ignore()

        self.mainwin.setDisabled(False)

    @AutomationFunctionDecorator
    def keyPressEvent(self, a0: QKeyEvent) -> None:
        
        KEY_ENTER = 16777220
        KEY_SUB_ENTER = 16777221

        print (f"a0.key() : {a0.key()}")
        if a0.key() == KEY_ENTER or a0.key() == KEY_SUB_ENTER:
            self.ok_Button_clicked(None)
        elif a0.key == KEY_ENTER:
            self.cancel_Button_clicked()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = UI_TestList()
    w.setupUi_Test()
    sys.exit(app.exec_())