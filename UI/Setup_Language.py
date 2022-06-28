# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_language.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication


class UI_Setup_Language(QWidget):
    def __init__(self):
        super().__init__()

    def setupUi_Language(self):
        self.setObjectName("Form")
        self.resize(744, 412)
        self.addLang_Button = QtWidgets.QPushButton(self)
        self.addLang_Button.setGeometry(QtCore.QRect(307, 10, 130, 31))
        self.addLang_Button.setObjectName("addLang_Button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 701, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.langList_VBoxLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.langList_VBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.langList_VBoxLayout.setObjectName("langList_VBoxLayout")
        self.border()
        self.langList_VBoxLayout.addWidget(self.lbl_border)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(560, 370, 161, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ok_Button.setObjectName("ok_Button")
        self.horizontalLayout.addWidget(self.ok_Button)
        self.cancel_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout.addWidget(self.cancel_Button)

        self.retranslateUi_language()
        # QtCore.QMetaObject.connectSlotsByName()

        # self.set_slot()
        self.show()

    def retranslateUi_language(self):
        self.setWindowTitle("언어 설정")
        self.addLang_Button.setText("언어 추가")
        self.ok_Button.setText("확인")
        self.cancel_Button.setText("취소")

    def border(self):
        self.lbl_border = QtWidgets.QLabel('')
        self.lbl_border.setStyleSheet("color: gray;"
                             "border-style: solid;"
                             "border-width: 1px;"
                             "border-color: #747474;"
                             "border-radius: 1px")

    # def set_slot(self):
        
    #     self.ok_Button.clicked.connect(QCoreApplication.instance().quit)
    #     self.cancel_Button.clicked.connect(self.onCancelButtonClicked, QCloseEvent)

    def closeEvent(self, QCloseEvent):
        re = QMessageBox.question(self, "변경사항 알림", "변경사항이 있습니다. \n이대로 종료하시겠습니까?",
                    QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()  



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = UI_Setup_Language()
    w.setupUi_Language()
    # Form = QtWidgets.QWidget()
    # ui = UI_Setup_Language()
    # ui.setupUi_Language(Form)
    # w.show()
    sys.exit(app.exec_())
