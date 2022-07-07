# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_language.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot


class UI_Setup_Language(QWidget):
    def __init__(self):
        super().__init__()
        self.cnt = 0

    def setupUi_Language(self):
        # 언어별 경로 설정 메인 창
        self.resize(744, 412)
        self.setWindowTitle("언어별 경로 설정")

        # 전체 화면 배치
        self.verticalLayout = QVBoxLayout(self)

        # [언어 추가], 언어 설정 리스트 영역 배치
        self.top_verticalLayout = QVBoxLayout()

        # [언어 추가] 버튼
        self.sl_editLang_horizontalLayout = QHBoxLayout()
        self.sl_editLang_horizontalLayout.setAlignment(Qt.AlignCenter)
        self.addLang_Button = QPushButton("언어 추가", self)
        self.addLang_Button.setMaximumWidth(130)
        self.sl_editLang_horizontalLayout.addWidget(self.addLang_Button)
        # self.delLang_Button = QPushButton("삭제", self)
        # self.delLang_Button.setMaximumWidth(130)
        # self.sl_editLang_horizontalLayout.addWidget(self.delLang_Button)
        self.top_verticalLayout.addLayout(self.sl_editLang_horizontalLayout)

        # 언어 설정 리스트 영역
        self.langList_scrollArea = QScrollArea(self)
        self.langList_scrollArea.setWidgetResizable(True)
        self.langList_scrollAreaWidgetContents = QWidget()
        self.langList_scrollAreaWidgetContents.setGeometry(QtCore.QRect(20, 50, 701, 311))
        self.langListScroll_verticalLayout = QVBoxLayout(self.langList_scrollAreaWidgetContents)
        self.langListScroll_verticalLayout.setAlignment(Qt.AlignTop)

        self.langList_scrollArea.setWidget(self.langList_scrollAreaWidgetContents)
        self.top_verticalLayout.addWidget(self.langList_scrollArea)
        self.verticalLayout.addLayout(self.top_verticalLayout)

        
        # [확인], [취소] 버튼
        self.sl_ok_horizontalLayout = QHBoxLayout()
        self.sl_ok_horizontalLayout.setAlignment(Qt.AlignRight)
        
        self.ok_Button = QPushButton("확인", self)
        self.sl_ok_horizontalLayout.addWidget(self.ok_Button)
        self.cancel_Button = QPushButton("취소", self)
        self.sl_ok_horizontalLayout.addWidget(self.cancel_Button)
        self.verticalLayout.addLayout(self.sl_ok_horizontalLayout)

        # 버튼 이벤트 함수
        self.sl_set_slot()

    def sl_set_slot(self):
        self.addLang_Button.clicked.connect(self.addLang_Button_clicked)

    def addLang_Button_clicked(self):
        self.langList_scrollArea.setWidget(self.langList_scrollAreaWidgetContents)
        self.top_verticalLayout.addWidget(self.langList_scrollArea)

        globals()[f'self.langList_horizontalLayout{self.cnt}'] = QHBoxLayout()

        # 삭제 버튼
        globals()[f'self.del_langList_button{self.cnt}'] = QPushButton("-", self.langList_scrollAreaWidgetContents)
        globals()[f'self.del_langList_button{self.cnt}'].setMaximumWidth(30)
        globals()[f'self.del_langList_button{self.cnt}'].clicked.connect(partial(self.del_langList_button_clicked, self.cnt))
        globals()[f'self.langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.del_langList_button{self.cnt}'])

        # 언어 입력
        globals()[f'self.lang_lineEdit{self.cnt}'] = QLineEdit(self.langList_scrollAreaWidgetContents)
        globals()[f'self.lang_lineEdit{self.cnt}'].setMaximumWidth(100)
        globals()[f'self.langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.lang_lineEdit{self.cnt}'])

        # 경로 입력
        globals()[f'self.dir_lineEdit{self.cnt}'] = QLineEdit(self.langList_scrollAreaWidgetContents)
        globals()[f'self.langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.dir_lineEdit{self.cnt}'])

        # 경로 검색 버튼
        globals()[f'self.langList_toolButton{self.cnt}'] = QToolButton(self.langList_scrollAreaWidgetContents)
        globals()[f'self.langList_toolButton{self.cnt}'].setText("...")
        globals()[f'self.langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'self.langList_toolButton{self.cnt}'])
        globals()[f'self.langList_toolButton{self.cnt}'].clicked.connect(partial(self.langList_toolButton_clicked, self.cnt))

        self.langListScroll_verticalLayout.addLayout(globals()[f'self.langList_horizontalLayout{self.cnt}'])

        self.cnt += 1
        
        self.langList_scrollArea.setWidget(self.langList_scrollAreaWidgetContents)
        self.top_verticalLayout.addWidget(self.langList_scrollArea)

    def del_langList_button_clicked(self, cnt):
        """라인 삭제 함수

        Args:
            cnt: 변수명
        """
        for i in range(globals()[f'self.langList_horizontalLayout{cnt}'].count()):
            globals()[f'self.langList_horizontalLayout{cnt}'].itemAt(i).widget().deleteLater()

    def langList_toolButton_clicked(self, cnt):
        """폴더 경로 불러오기

        Args:
            cnt: 변수명
        """
        folderPath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        globals()[f'self.dir_lineEdit{cnt}'].setText(folderPath)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_Setup_Language()
    ui.setupUi_Language()
    ui.show()
    sys.exit(app.exec_())
