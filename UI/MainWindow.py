# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.resize(1472, 876)
        self.setWindowTitle("다국어 자동화")

        # 전체 화면 배치
        self.horizontalLayout = QHBoxLayout()

        # 좌측 이미지 리스트
        self.img_VBoxLayout = QVBoxLayout()
        self.img_VBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.border()
        self.img_VBoxLayout.addWidget(self.lbl_border)
        self.horizontalLayout.addLayout(self.img_VBoxLayout)

        # 우측 큰 이미지
        
        self.img_Label = QLabel(self)
        self.img_Label.setGeometry(QtCore.QRect(90, 10, 1350, 600))
        self.img_Label.setStyleSheet("color: gray;"
                             "border-style: solid;"
                             "border-width: 1px;"
                             "border-color: #747474;"
                             "border-radius: 1px")

        # 이미지 설명, 스크립트명
        self.desc_gridLayoutWidget = QWidget(self)
        self.desc_gridLayoutWidget.setGeometry(QtCore.QRect(300, 620, 675, 50))
        self.desc_gridLayout = QGridLayout(self.desc_gridLayoutWidget)
        self.desc_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.desc_Label = QtWidgets.QLabel(self.desc_gridLayoutWidget)
        self.desc_Label.setText("이미지 설명")
        self.desc_gridLayout.addWidget(self.desc_Label, 0,0,1,1)
        self.desc_LineEdit = QLineEdit(self.desc_gridLayoutWidget)
        self.desc_gridLayout.addWidget(self.desc_LineEdit, 0,1,1,1)
        self.scripts_Label = QLabel(self.desc_gridLayoutWidget)
        self.scripts_Label.setText("스크립트명")
        self.desc_gridLayout.addWidget(self.scripts_Label, 1,0,1,1)
        self.scripts_LineEdit = QLineEdit(self.desc_gridLayoutWidget)
        self.desc_gridLayout.addWidget(self.scripts_LineEdit, 1,1,1,1)

        # 평가 목록
        self.testList_groupbox = QGroupBox("평가 목록", self)
        self.testList_groupbox.setGeometry(QtCore.QRect(90, 680, 1141, 151))
        self.testList_groupbox.setContentsMargins(0, 0, 0, 0)

        self.testList_horizontalLayoutWidget = QWidget(self.testList_groupbox)
        self.testList_Layout = QHBoxLayout(self.testList_horizontalLayoutWidget)
        self.testList_Layout.setContentsMargins(0, 0, 0, 0)

        # 저장 버튼
        self.save_Button = QPushButton("저장", self)
        self.save_Button.setGeometry(QtCore.QRect(1280, 650, 131, 31))

        # ALL PASS, ALL FAIL, ALL N/T, ALL N/A
        self.verticalLayoutWidget_2 = QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1300, 690, 161, 141))
        self.testAll_VBoxLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.testAll_VBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.allPass_RadioButton = QRadioButton("ALL PASS", self.verticalLayoutWidget_2)
        self.testAll_VBoxLayout.addWidget(self.allPass_RadioButton)
        self.allNA_RadioButton = QRadioButton("ALL N/A", self.verticalLayoutWidget_2)
        self.testAll_VBoxLayout.addWidget(self.allNA_RadioButton)
        self.allNT_RadioButton = QRadioButton("ALL N/T", self.verticalLayoutWidget_2)
        self.testAll_VBoxLayout.addWidget(self.allNT_RadioButton)
        self.allFail_RadioButton = QRadioButton("ALL FAIL", self.verticalLayoutWidget_2)
        self.testAll_VBoxLayout.addWidget(self.allFail_RadioButton)

        self.menubar = self.menuBar()
        
        self.menu = self.menubar.addMenu("Menu")

        self.actionOpen = QAction("Open", self)
        self.actionCreateExcel = QAction("Create Excel", self)
        self.actionClose = QAction("Close", self)
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionCreateExcel)
        self.menu.addAction(self.actionClose)

        self.setup = self.menubar.addMenu("Setup")
        self.actionLanguage = QAction("Language", self)
        self.actionTest_List = QAction("Test List", self)
        self.actionExcel_Setting = QAction("Excel Setting", self)
        self.setup.addAction(self.actionLanguage)
        self.setup.addAction(self.actionTest_List)
        self.setup.addAction(self.actionExcel_Setting)

    def border(self):
        self.lbl_border = QtWidgets.QLabel('')
        self.lbl_border.setStyleSheet("color: gray;"
                             "border-style: solid;"
                             "border-width: 1px;"
                             "border-color: #747474;"
                             "border-radius: 1px")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    # ui.setupUi()
    # ui.show()
    sys.exit(app.exec_())
