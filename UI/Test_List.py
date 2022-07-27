from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from functools import partial
from Database.DB import DBManager
from UI import MainWindow

class Ui_Test_List(QWidget, DBManager):
    def __init__(self, mainwindow):
        super().__init__()

        self.save_List = []
        self.key = []
        self.mainwin = mainwindow
        self.Bool_start = True
        self.Bool_quit = False

    def setupUi_Test(self):

        if (self.Bool_start) :
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
            self.Bool_start = False

    def btn_set_slot(self):
        self.addTest_Button.clicked.connect(partial(self.addTest_Button_clicked, val = None)) # 0719
        self.ok_Button.clicked.connect(self.ok_Button_clicked)
        self.cancel_Button.clicked.connect(self.cancel_Button_clicked)

    def setTest_Button(self):

        self.cnt = 0
        # 중복제거 중간점검
        self.c.execute(f"SELECT 평가목록 FROM Test_List")
        List = self.c.fetchall()

        if List != NULL and len(self.TestListScroll_verticalLayout) != 0:

            item_list = list(range(self.TestListScroll_verticalLayout.count()))
            item_list.reverse()#  Reverse delete , Avoid affecting the layout order 

            print(item_list)
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

        print(List)
        for val in List:

            val = str(val)
            val = val[2 : val.find(",")- 1]
            self.addTest_Button_clicked(val= val)

    def addTest_Button_clicked(self, val):

        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)

        globals()[f'TestList_horizontalLayout{self.cnt}'] = QHBoxLayout()

        # 삭제 버튼
        globals()[f'del_TestList_btn{self.cnt}'] = QPushButton("-", self.TestList_scrollAreaWidgetContents)
        globals()[f'del_TestList_btn{self.cnt}'].setMaximumWidth(30)
        globals()[f'del_TestList_btn{self.cnt}'].clicked.connect(partial(
            self.del_TestList_btn_clicked, layout = globals()[f'TestList_horizontalLayout{self.cnt}']))
        
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

    def del_TestList_btn_clicked(self, layout):
        """라인 삭제 함수

        Args:
            cnt: 변수명
        """

        self.Bool_quit = True # 0719

        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

    def ok_Button_clicked(self):

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
        for i in range(self.cnt):
            try:
                self.dbConn.execute(f"INSERT INTO Test_List VALUES (?)", 
                        (globals()[f'Test_lineEdit{i}'].text(),))
                self.dbConn.commit()
            except RuntimeError:
                continue

        self.mainwin.setWidget_func()
        self.close()

    def cancel_Button_clicked(self):

        self.close()

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

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        
        KEY_ENTER = 16777220

        print (f"a0.key() : {a0.key()}")
        if a0.key() == KEY_ENTER:
            self.ok_Button_clicked()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_Test_List()
    w.setupUi_Test()
    sys.exit(app.exec_())