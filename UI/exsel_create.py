"""
1. 큰 위젯기준으로 레이아웃2개 분리
1-2 지금까지 평가했던 평가항목들 스캔하기 그룹라디오
2. 분리된 레이아웃중 하나는 새로만드는것
3. 2번쟤꺼는 기존에 레이아웃에 추가하는것
"""
from msilib.schema import RadioButton
from tabnanny import check
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Database.DB import DBManager
from functools import partial
import sys
import os
class Ui_exsel_create(QWidget, DBManager):

    def __init__(self):
        super().__init__()
        DBManager().__init__()
        self.Bool_start = True
        

    def setupUi(self):

        if (self.Bool_start) :

            self.setFixedSize(400, 420)
            self.setWindowTitle("엑셀 생성")

            # 전체 화면 배치
            self.hBoxLayout = QHBoxLayout(self)
            self.vBoxLayout = QVBoxLayout(self)

            self.checkQGroupBox = QGroupBox("언어 선택")
            self.checkQGroupBox.setFixedSize(80,420)
            self.langSetting()
            self.hBoxLayout.addWidget(self.checkQGroupBox)

            self.radio_vbox = QVBoxLayout()
            self.radioQGroupBox = QGroupBox("신규 및 기존 엑셀 생성")

            self.new_excel_groupBox = QGroupBox("신규 엑셀 생성")
            self.new_excel_groupBox.setCheckable(True)
            self.new_excel_groupBox.setMaximumSize(290,70)
            self.new_excel_groupBox.clicked.connect(
                lambda : self.func_new_excel_groupBox())
            self.new_exsel_func()
            
            self.set_excel_groupBox = QGroupBox("기존 엑셀 편집")
            self.set_excel_groupBox.setCheckable(True)
            self.set_excel_groupBox.setMaximumSize(290,70)
            self.set_excel_groupBox.clicked.connect(
                lambda : self.func_set_excel_groupBox())
            self.set_exsel_func()

            self.new_excel_groupBox.setChecked(True)
            self.set_excel_groupBox.setChecked(False)

            self.radioQGroupBox.setLayout(self.radio_vbox)

            self.vBoxLayout.addWidget(self.radioQGroupBox)

            # 확인_취소
            self.create_exsel = QWidget()
            self.create_exsel.setFixedSize(292,80)
            check_cencel = QVBoxLayout()
            check = QPushButton("생성")
            cencel = QPushButton("취소")
            check_cencel.addWidget(check)
            check_cencel.addWidget(cencel)
            self.create_exsel.setLayout(check_cencel)

            self.vBoxLayout.addWidget(self.create_exsel)

            self.hBoxLayout.addLayout(self.vBoxLayout)

    def langSetting(self):

        self.c.execute('SELECT * FROM Setup_Language')
        dataList = self.c.fetchall()

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop)
        the_check = QCheckBox("전체")
        vbox.addWidget(the_check)

        for val in dataList:
            print(val[0])

            globals()[f'checkBox_{val[0]}'] = QCheckBox(val[0])
            globals()[f'checkBox_{val[0]}'].clicked.connect(lambda : func_checkbox())
            vbox.addWidget(globals()[f'checkBox_{val[0]}'])

        the_check.clicked.connect(lambda : func_check())

        self.checkQGroupBox.setLayout(vbox)

        def func_check():

            if (the_check.isChecked() == True):
                for val in dataList:
                    globals()[f'checkBox_{val[0]}'].setChecked(True)
            elif (the_check.isChecked() == False):
                for val in dataList:
                    globals()[f'checkBox_{val[0]}'].setChecked(False)

        def func_checkbox():

            if (the_check.isChecked() == True):
                for val in dataList:

                    if (globals()[f'checkBox_{val[0]}'].isChecked() == False):
                        the_check.setChecked(False)

            elif (the_check.isChecked() == False):

                result = []

                for val in dataList:

                    result.append(globals()[f'checkBox_{val[0]}'].isChecked())

                if (result.count(False) == 0):
                    the_check.setChecked(True)
            
    def new_exsel_func(self):

        # 엑셀 경로 라벨
        path_hbox = QHBoxLayout()
        edit_path = QLineEdit()
        path_btn = QPushButton()
        path_btn.setMaximumWidth(30)
        path_btn.setText("...")

        path_btn.clicked.connect(partial(self.langList_toolButton_clicked, edit = edit_path))
        path_hbox.addWidget(edit_path)
        path_hbox.addWidget(path_btn)

        self.new_excel_groupBox.setLayout(path_hbox)
        self.radio_vbox.addWidget(self.new_excel_groupBox)

    def set_exsel_func(self):

        # 엑셀 경로 라벨
        path_hbox = QHBoxLayout()
        edit_path = QLineEdit()
        path_btn = QPushButton()
        path_btn.setMaximumWidth(30)
        path_btn.setText("...")
        
        path_btn.clicked.connect(partial(self.langList_toolButton_clicked, edit = edit_path))

        path_hbox.addWidget(edit_path)
        path_hbox.addWidget(path_btn)
        self.set_excel_groupBox.setLayout(path_hbox)
        self.radio_vbox.addWidget(self.set_excel_groupBox)

    def langList_toolButton_clicked(self, edit):
        """폴더 경로 불러오기

        Args:
            cnt: 변수명
        """
        folderPath = QFileDialog.getExistingDirectory(self, 'Find Folder')

        print(f"folderPath : {folderPath}")

        edit.setText(str(folderPath))


    def func_new_excel_groupBox(self):

        if (self.new_excel_groupBox.isChecked() == True):
            self.new_excel_groupBox.setChecked(True)
            self.set_excel_groupBox.setChecked(False)
        else:
            self.new_excel_groupBox.setChecked(False)
            self.set_excel_groupBox.setChecked(True)

    def func_set_excel_groupBox(self):

        if (self.set_excel_groupBox.isChecked() == True):
            self.set_excel_groupBox.setChecked(True)
            self.new_excel_groupBox.setChecked(False)
        else:
            self.set_excel_groupBox.setChecked(False)
            self.new_excel_groupBox.setChecked(True)

 

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Ui_exsel_create()
    sys.exit(app.exec_())
