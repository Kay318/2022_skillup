from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from functools import partial
from Database.DB import DBManager
from UI import MainWindow

class Ui_Test_List(QWidget, DBManager):
    def __init__(self, mainwindow):
        super().__init__()
        DBManager().__init__()

        self.cnt = 0
        self.save_List = []
        self.key = []
        self.mainwin = mainwindow
        self.Bool_start = True

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
            # self.setTest_Button()
            self.btn_set_slot()

            self.fill_verticalLayout.addWidget(self.add_btn_QWidget)
            self.fill_verticalLayout.addWidget(self.set_QWidget)
            self.fill_verticalLayout.addWidget(self.set_btn_QWidget)
            self.setLayout(self.fill_verticalLayout)
            self.show()
            self.Bool_start = False

    def btn_set_slot(self):
        self.addTest_Button.clicked.connect(self.addTest_Button_clicked)
        self.ok_Button.clicked.connect(self.ok_Button_clicked)
        self.cancel_Button.clicked.connect(self.cancel_Button_clicked)

    def setTest_Button(self):

        # 중복제거 중간점검
        self.c.execute(f"SELECT 평가목록 FROM Test_List")
        List = self.c.fetchall()

        self.cnt = 0

        if List != NULL and len(self.TestListScroll_verticalLayout) != 0:

            item_list = list(range(self.TestListScroll_verticalLayout.count()))
            item_list.reverse()#  Reverse delete , Avoid affecting the layout order 

            for i in item_list:
                item = self.TestListScroll_verticalLayout.itemAt(i)
                self.TestListScroll_verticalLayout.removeItem(item)
                if item.widget():
                    item.widget().deleteLater()

        for val in List:

            val = str(val)

            self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.TestList_scrollArea)

            globals()[f'self.TestList_horizontalLayout{self.cnt}'] = QHBoxLayout()

            # 삭제 버튼
            globals()[f'self.del_TestList_btn{self.cnt}'] = QPushButton("-", self.TestList_scrollAreaWidgetContents)
            globals()[f'self.del_TestList_btn{self.cnt}'].setMaximumWidth(30)
            globals()[f'self.del_TestList_btn{self.cnt}'].clicked.connect(partial(
                self.del_TestList_btn_clicked, layout = globals()[f'self.TestList_horizontalLayout{self.cnt}'], cnt = self.cnt))
            
            # 내용 입력
            globals()[f'self.Test_lineEdit{self.cnt}'] = QLineEdit(self.TestList_scrollAreaWidgetContents)
            globals()[f'self.Test_lineEdit{self.cnt}'].setMaximumWidth(300)
            globals()[f'self.Test_lineEdit{self.cnt}'].setText(val[2 : val.find(",")- 1])

            globals()[f'self.TestList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.del_TestList_btn{self.cnt}'])
            globals()[f'self.TestList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.Test_lineEdit{self.cnt}'])

            self.TestListScroll_verticalLayout.addLayout(globals()[f'self.TestList_horizontalLayout{self.cnt}'])

            self.cnt += 1

            print("호출당한 횟수ㅣ%s", self.cnt)
            
            self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.TestList_scrollArea)

    def addTest_Button_clicked(self):

        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)

        globals()[f'self.TestList_horizontalLayout{self.cnt}'] = QHBoxLayout()

        # 삭제 버튼
        globals()[f'self.del_TestList_btn{self.cnt}'] = QPushButton("-", self.TestList_scrollAreaWidgetContents)
        globals()[f'self.del_TestList_btn{self.cnt}'].setMaximumWidth(30)
        globals()[f'self.del_TestList_btn{self.cnt}'].clicked.connect(partial(
            self.del_TestList_btn_clicked, layout = globals()[f'self.TestList_horizontalLayout{self.cnt}'], cnt = self.cnt))
        
        # 내용 입력
        globals()[f'self.Test_lineEdit{self.cnt}'] = QLineEdit(self.TestList_scrollAreaWidgetContents)
        globals()[f'self.Test_lineEdit{self.cnt}'].setMaximumWidth(300)

        globals()[f'self.TestList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.del_TestList_btn{self.cnt}'])
        globals()[f'self.TestList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.Test_lineEdit{self.cnt}'])

        self.TestListScroll_verticalLayout.addLayout(globals()[f'self.TestList_horizontalLayout{self.cnt}'])

        self.cnt += 1

        print("호출당한 횟수ㅣ%s", self.cnt)
        
        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)


    def del_TestList_btn_clicked(self, layout, cnt):
        """라인 삭제 함수

        Args:
            cnt: 변수명
        """
        print(f"결과 : {globals()[f'self.Test_lineEdit{cnt}'].text()}")

        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

    def ok_Button_clicked(self):

        checkOverlap = []

        # 빈칸 및 중복 언어 체크
        for i in range(self.cnt):
            try:
                if globals()[f'self.Test_lineEdit{i}'].text() == "":
                    QMessageBox.about(self, '주의', '빈칸이 있습니다. \n 확인해 주세요.')
                    return
            except RuntimeError:
                continue

            if (globals()[f'self.Test_lineEdit{i}'].text() not in checkOverlap):
                checkOverlap.append(globals()[f'self.Test_lineEdit{i}'].text())
            else:
                QMessageBox.about(self, '주의', f'{i+1}번째 라인이 중복으로 입력되었습니다.')
                return

        # DB에 저장
        self.c.execute(f"DELETE FROM Test_List")
        for i in range(self.cnt):
            try:
                self.dbConn.execute(f"INSERT INTO Test_List VALUES (?)", 
                        (globals()[f'self.Test_lineEdit{i}'].text(),))
                self.dbConn.commit()
            except RuntimeError:
                continue
        
        self.mainwin.setEnabled(True)
        self.mainwin.setWidget_func()
        
        self.close()

    def cancel_Button_clicked(self):

        self.mainwin.setEnabled(True)
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_Test_List()
    w.setupUi_Test()
    sys.exit(app.exec_())