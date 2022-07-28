# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_language.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QKeyEvent
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
from Database.DB import DBManager


class UI_Setup_Language(QWidget, DBManager):
    def __init__(self, mainwindow):
        super().__init__()
        self.start = True
        self.mainwin = mainwindow

    def setupUi_Language(self):
        # 언어별 경로 설정 메인 창
        if self.start:
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

        self.start = False

    def sl_set_slot(self):
        self.addLang_Button.clicked.connect(partial(self.addLang_Button_clicked, btn_data = None))
        self.ok_Button.clicked.connect(self.ok_Button_clicked)
        self.cancel_Button.clicked.connect(self.close)

    # 0728
    def setLang_Button(self):

        self.cnt = 0

        # DB에서 언어 설정 불러옴
        self.c.execute('SELECT * FROM Setup_Language')
        dataList = self.c.fetchall()

        if dataList != None and len(self.langListScroll_verticalLayout) != 0:

                item_list = list(range(self.langListScroll_verticalLayout.count()))
                item_list.reverse()#  Reverse delete , Avoid affecting the layout order 

                for i in item_list:

                    item = self.langListScroll_verticalLayout.itemAt(i)
                    self.langListScroll_verticalLayout.removeItem(item)
                    if item.widget():
                        item.widget().deleteLater()

        for data in dataList:

            self.addLang_Button_clicked(data)

    # 0728
    def addLang_Button_clicked(self, btn_data):

        lang_line_text = ""
        dir_line_text = ""
        self.langList_scrollArea.setWidget(self.langList_scrollAreaWidgetContents)
        self.top_verticalLayout.addWidget(self.langList_scrollArea)
        
        if btn_data != None :
            lang_line_text = btn_data[0]
            dir_line_text = btn_data[1]

        globals()[f'langList_horizontalLayout{self.cnt}'] = QHBoxLayout()

        # 삭제 버튼
        globals()[f'del_langList_button{self.cnt}'] = QPushButton("-", self.langList_scrollAreaWidgetContents)
        globals()[f'del_langList_button{self.cnt}'].setMaximumWidth(30)
        globals()[f'del_langList_button{self.cnt}'].clicked.connect(partial(
            self.del_langList_button_clicked, layout = globals()[f'langList_horizontalLayout{self.cnt}'], cnt = self.cnt)) # 0728
        globals()[f'langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'del_langList_button{self.cnt}'])

        # 언어 입력
        globals()[f'lang_lineEdit{self.cnt}'] = QLineEdit(self.langList_scrollAreaWidgetContents)
        globals()[f'lang_lineEdit{self.cnt}'].setMaximumWidth(100)
        globals()[f'lang_lineEdit{self.cnt}'].setPlaceholderText('언어 입력')
        globals()[f'lang_lineEdit{self.cnt}'].setText(lang_line_text)
        globals()[f'langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'lang_lineEdit{self.cnt}'])

        # 경로 입력
        globals()[f'dir_lineEdit{self.cnt}'] = QLineEdit(self.langList_scrollAreaWidgetContents)
        globals()[f'dir_lineEdit{self.cnt}'].setPlaceholderText('우측 버튼으로 폴더 경로 설정')
        globals()[f'dir_lineEdit{self.cnt}'].setText(dir_line_text)
        globals()[f'langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'dir_lineEdit{self.cnt}'])

        # 경로 검색 버튼
        globals()[f'langList_toolButton{self.cnt}'] = QToolButton(self.langList_scrollAreaWidgetContents)
        globals()[f'langList_toolButton{self.cnt}'].setText("...")
        globals()[f'langList_horizontalLayout{self.cnt}'].addWidget(globals()[f'langList_toolButton{self.cnt}'])
        globals()[f'langList_toolButton{self.cnt}'].clicked.connect(partial(self.langList_toolButton_clicked, globals()[f'dir_lineEdit{self.cnt}']))

        for val in range(self.cnt + 1):

            if globals()[f'lang_lineEdit{val}'].text() == "":
                globals()[f'lang_lineEdit{val}'].setFocus()
                break
            
        self.langListScroll_verticalLayout.addLayout(globals()[f'langList_horizontalLayout{self.cnt}'])

        self.cnt += 1
        
        self.langList_scrollArea.setWidget(self.langList_scrollAreaWidgetContents)
        self.top_verticalLayout.addWidget(self.langList_scrollArea)

    # 0728
    def del_langList_button_clicked(self, layout, cnt):
        """라인 삭제 함수

        Args:
            cnt: 변수명
        """

        self.Bool_quit = True # 0719

        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

        item_list = list(range(self.langListScroll_verticalLayout.count()))
        item_list.reverse()#  Reverse delete , Avoid affecting the layout order 

        for i in item_list:

            item = self.langListScroll_verticalLayout.itemAt(i)

            if (layout == item):
                print("PASS")
                self.langListScroll_verticalLayout.removeItem(item)

    def langList_toolButton_clicked(self, lineEdit):
        """폴더 경로 불러오기

        Args:
            cnt: 변수명
        """
        folderPath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        lineEdit.setText(folderPath)

    def ok_Button_clicked(self):
        checkOverlap = []

        # 빈칸 및 중복 언어 체크
        for i in range(self.cnt):
            try:
                if globals()[f'lang_lineEdit{i}'].text() == "" or globals()[f'dir_lineEdit{i}'].text() == "":
                    QMessageBox.about(self, '주의', '빈칸이 있습니다. \n 확인해 주세요.')
                    return
            except RuntimeError:
                continue

            if (globals()[f'lang_lineEdit{i}'].text() not in checkOverlap and
                globals()[f'dir_lineEdit{i}'].text() not in checkOverlap):
                checkOverlap.append(globals()[f'lang_lineEdit{i}'].text())
                checkOverlap.append(globals()[f'dir_lineEdit{i}'].text())
            else:
                QMessageBox.about(self, '주의', '중복 라인이 있습니다.')
                return

        # DB에 저장
        self.c.execute(f"DELETE FROM Setup_Language")

        if self.langListScroll_verticalLayout.count() != 0:
            for i in range(self.cnt):
                try:
                    self.dbConn.execute(f"INSERT INTO Setup_Language VALUES (?, ?)", 
                            (globals()[f'lang_lineEdit{i}'].text(), globals()[f'dir_lineEdit{i}'].text()))
                except RuntimeError:
                    continue

        self.dbConn.commit()
        
        self.mainwin.show()

        self.close()

    def closeEvent(self, event) -> None:
        self.c.execute('SELECT * FROM Setup_Language')
        dataList = self.c.fetchall()

        dbList = [data for data in dataList]
        langList = []
        dirList = []
        
        for i in range(self.cnt):
            try:
                langList.append(globals()[f'lang_lineEdit{i}'].text())
                dirList.append(globals()[f'dir_lineEdit{i}'].text())
            except RuntimeError:
                continue

        lineList = [i for i in zip(langList, dirList)]

        if dbList != lineList:
            reply = QMessageBox.question(self, '알림', '변경사항이 있습니다.\n취소하시겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

        langList.clear()
        self.mainwin.setDisabled(False)

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        
        KEY_ENTER = 16777220

        print (f"a0.key() : {a0.key()}")
        if a0.key() == KEY_ENTER:
            self.ok_Button_clicked()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_Setup_Language()
    ui.setupUi_Language()
    ui.show()
    sys.exit(app.exec_())
