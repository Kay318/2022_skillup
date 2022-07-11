from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from functools import partial

class Ui_Test_List(QWidget):
    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.func_cnt = 0

    def setupUi_Test(self):
        if self.func_cnt == 0:
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
            self.show()
        
        self.func_cnt += 1

    def btn_set_slot(self):
        self.addTest_Button.clicked.connect(self.addTest_Button_clicked)
        
    def addTest_Button_clicked(self):

        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)

        locals()[f'self.TestList_horizontalLayout{self.cnt}'] = QHBoxLayout()

        # LineText
        locals()[f'self.Test_TextEdit{self.cnt}'] = QLabel(self.TestList_scrollAreaWidgetContents)
        locals()[f'self.Test_TextEdit{self.cnt}'].setMaximumWidth(50)
        locals()[f'self.Test_TextEdit{self.cnt}'].setMaximumHeight(20)
        locals()[f'self.Test_TextEdit{self.cnt}'].setText(f'조건 : ')
        locals()[f'self.TestList_horizontalLayout{self.cnt}'].addWidget(locals()[f'self.Test_TextEdit{self.cnt}'])
        
        # 내용 입력
        locals()[f'self.Test_lineEdit{self.cnt}'] = QLineEdit(self.TestList_scrollAreaWidgetContents)
        locals()[f'self.Test_lineEdit{self.cnt}'].setMaximumWidth(250)
        locals()[f'self.TestList_horizontalLayout{self.cnt}'].addWidget(locals()[f'self.Test_lineEdit{self.cnt}'])

        # 삭제 버튼
        locals()[f'self.del_TestList_btn{self.cnt}'] = QPushButton("del", self.TestList_scrollAreaWidgetContents)
        locals()[f'self.del_TestList_btn{self.cnt}'].setMaximumWidth(30)
        locals()[f'self.del_TestList_btn{self.cnt}'].clicked.connect(partial(
            self.del_TestList_btn_clicked, layout = locals()[f'self.TestList_horizontalLayout{self.cnt}']))

        locals()[f'self.TestList_horizontalLayout{self.cnt}'].addWidget(locals()[f'self.del_TestList_btn{self.cnt}'])

        self.TestListScroll_verticalLayout.addLayout(locals()[f'self.TestList_horizontalLayout{self.cnt}'])

        self.cnt += 1
        
        self.TestList_scrollArea.setWidget(self.TestList_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.TestList_scrollArea)

    def del_TestList_btn_clicked(self, layout):
        """라인 삭제 함수

        Args:
            cnt: 변수명
        """
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_Test_List()
    w.setupUi_Test()
    sys.exit(app.exec_())