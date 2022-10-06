"""
1. 큰 위젯기준으로 레이아웃2개 분리
1-2 지금까지 평가했던 평가항목들 스캔하기 그룹라디오
2. 분리된 레이아웃중 하나는 새로만드는것
3. 2번쟤꺼는 기존에 레이아웃에 추가하는것
"""

from Screen.excel_control import excelModul
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Database.DB import DBManager
from functools import partial
import sys
from Helper import *

class UI_CreateExcel(QWidget, DBManager):

    def __init__(self, mainwindow):
        super().__init__()
        self.mainwin = mainwindow
        self.new_excel_path = ""
        self.set_excel_path = ""

    @AutomationFunctionDecorator
    def setupUI_CreateExcel(self):

        self.setFixedSize(400, 420)
        self.setWindowTitle("엑셀 생성")

        # 전체 화면 배치
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.lang_vbox = QVBoxLayout()
        self.checkQ_label = QLabel()
        self.lang_widget = QWidget()
        self.lang_scroll =QScrollArea()
        self.lang_data_vbox = QVBoxLayout(self)
        self.checkQ_label.setText("언어 설정")
        self.lang_vbox.addWidget(self.checkQ_label)
        self.hBoxLayout.addLayout(self.lang_vbox)

        self.radioQGroupBox = QGroupBox("신규 및 기존 엑셀 생성")

        self.radio_vbox = QVBoxLayout()

        new_excel_label = QLabel()
        new_excel_label.setFixedHeight(80)
        font = QFont()
        font.setPixelSize(11)
        new_excel_label.setFont(font)
        new_excel_label.setAlignment(Qt.AlignTop)
        new_excel_label.setAlignment(Qt.AlignLeft)
        new_excel_label.setText(" 신규 엑셀 생성\n"
        " 현재 데이터를 기반으로 엑셀 파일을 새로 생성해\n"
        " 작성됩니다.")
        set_excel_label = QLabel()
        set_excel_label.setFont(font)
        set_excel_label.setText(" 기존 엑셀 편집\n"
        " 기존 데이터를 기반으로 현재 데이터로 편집되어\n"
        " 작성됩니다.")
        set_excel_label.setFixedHeight(80)
        set_excel_label.setAlignment(Qt.AlignTop)
        set_excel_label.setAlignment(Qt.AlignLeft)

        self.radio_vbox.addWidget(new_excel_label)
        self.new_excel_groupBox = QGroupBox("신규 엑셀 생성")
        self.new_excel_groupBox.setCheckable(True)
        self.new_excel_groupBox.setFixedSize(275,50)
        self.new_excel_groupBox.clicked.connect(
            lambda : self.func_new_excel_groupBox())
        self.new_excel_func()
        self.radio_vbox.addWidget(self.new_excel_groupBox)

        self.radio_vbox.addWidget(set_excel_label)
        self.set_excel_groupBox = QGroupBox("기존 엑셀 편집")
        self.set_excel_groupBox.setFixedSize(275,50)
        self.set_excel_groupBox.setCheckable(True)
        self.set_excel_groupBox.clicked.connect(
            lambda : self.func_set_excel_groupBox())
        self.set_excel_func()
        self.radio_vbox.addWidget(self.set_excel_groupBox)

        self.new_excel_groupBox.setChecked(True)
        self.set_excel_groupBox.setChecked(False)

        self.radioQGroupBox.setLayout(self.radio_vbox)

        self.vBoxLayout.addWidget(self.radioQGroupBox)

        # 확인_취소
        self.create_excel = QWidget()
        self.create_excel.setFixedSize(292,80)
        check_cencel = QVBoxLayout()
        check = QPushButton("생성")
        check.clicked.connect(partial(self.func_check))
        cencel = QPushButton("취소")
        cencel.clicked.connect(partial(self.func_cencel))
        check_cencel.addWidget(check)
        check_cencel.addWidget(cencel)
        self.create_excel.setLayout(check_cencel)

        self.vBoxLayout.addWidget(self.create_excel)

        self.hBoxLayout.addLayout(self.vBoxLayout)

    def langSetting(self):

        self.c.execute('SELECT * FROM Setup_Language')
        dataList = self.c.fetchall()

        self.lang_scroll.setFixedSize(80,380)
        self.lang_scroll.setWidgetResizable(True)
        self.lang_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lang_data_vbox.setAlignment(Qt.AlignTop)
        the_check = QCheckBox("전체")

        if dataList != None and len(self.lang_data_vbox) != 0:

            item_list = list(range(self.lang_data_vbox.count()))
            item_list.reverse()#  Reverse delete , Avoid affecting the layout order 

            for i in item_list:

                item = self.lang_data_vbox.itemAt(i)
                self.lang_data_vbox.removeItem(item)
                if item.widget():
                    item.widget().deleteLater()

        self.lang_data_vbox.addWidget(the_check)

        for val in dataList:

            print(f"val {val[0]}")
            globals()[f'checkBox_{val[0]}'] = QCheckBox(val[0])
            globals()[f'checkBox_{val[0]}'].clicked.connect(lambda : func_checkbox())
            self.lang_data_vbox.addWidget(globals()[f'checkBox_{val[0]}'])

        the_check.clicked.connect(lambda : func_check())
        print(f"self.lang_data_vbox : {self.lang_data_vbox.count()}")
        self.lang_widget.setLayout(self.lang_data_vbox)
        self.lang_scroll.setWidget(self.lang_widget)
        self.lang_vbox.addWidget(self.lang_scroll)

        def func_check():

            if (the_check.isChecked() == True):
                for val in dataList:
                    globals()[f'checkBox_{val[0]}'].setChecked(True)
                    self.lang_choice_list.append(val[0])
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
            
    @AutomationFunctionDecorator
    def new_excel_func(self):

        # 엑셀 경로 라벨
        path_hbox = QHBoxLayout()
        edit_path = QLineEdit()
        path_btn = QPushButton()
        path_btn.setMaximumWidth(30)
        path_btn.setText("...")

        path_btn.clicked.connect(partial(self.folder_toolButton_clicked, edit_path))
        path_hbox.addWidget(edit_path)
        path_hbox.addWidget(path_btn)

        self.new_excel_groupBox.setLayout(path_hbox)
        self.radio_vbox.addWidget(self.new_excel_groupBox)

    @AutomationFunctionDecorator
    def set_excel_func(self):

        # 엑셀 경로 라벨
        path_hbox = QHBoxLayout()
        edit_path = QLineEdit()
        path_btn = QPushButton()
        path_btn.setMaximumWidth(30)
        path_btn.setText("...")
        
        path_btn.clicked.connect(partial(self.langList_toolButton_clicked, edit_path))

        path_hbox.addWidget(edit_path)
        path_hbox.addWidget(path_btn)
        self.set_excel_groupBox.setLayout(path_hbox)
        self.radio_vbox.addWidget(self.set_excel_groupBox)

    @AutomationFunctionDecorator
    def langList_toolButton_clicked(self, edit, litter):
        """폴더 경로 불러오기

        Args:
            cnt: 변수명
        """
        folderPath = QFileDialog(self)
        folderPath.setFileMode(QFileDialog.FileMode.ExistingFile)
        folderPath.setNameFilter(self.tr("Data Files (*.csv *.xls *.xlsx);; All Files(*.*)"))
        folderPath.setViewMode(QFileDialog.ViewMode.Detail)
        if folderPath.exec_():
            fileNames = folderPath.selectedFiles()
            fileNames = str(fileNames)
            print(f"fileNames : {fileNames[2 : len(fileNames) - 2]}")
            fileNames = fileNames[2 : len(fileNames) - 2]

        print(f"folderPath : {folderPath}")

        edit.setText(str(fileNames))

        self.set_excel_path = fileNames

    @AutomationFunctionDecorator
    def folder_toolButton_clicked(self, edit, litter):
        """폴더 경로 불러오기

        Args:
            cnt: 변수명
        """

        folderPath = QFileDialog.getExistingDirectory(self, 'Find Folder')

        print(f"folderPath : {folderPath}")

        edit.setText(str(folderPath))

        self.new_excel_path = folderPath

    @AutomationFunctionDecorator
    def func_new_excel_groupBox(self):

        if (self.new_excel_groupBox.isChecked() == True):
            self.new_excel_groupBox.setChecked(True)
            self.set_excel_groupBox.setChecked(False)
        else:
            self.new_excel_groupBox.setChecked(False)
            self.set_excel_groupBox.setChecked(True)

    @AutomationFunctionDecorator
    def func_set_excel_groupBox(self):

        if (self.set_excel_groupBox.isChecked() == True):
            self.set_excel_groupBox.setChecked(True)
            self.new_excel_groupBox.setChecked(False)
        else:
            self.set_excel_groupBox.setChecked(False)
            self.new_excel_groupBox.setChecked(True)

    @AutomationFunctionDecorator
    def func_check(self, litter):

        self.c.execute('SELECT * FROM Setup_Language')
        dataList = self.c.fetchall()

        lang_choice_list = []

        for val in dataList:
            if (globals()[f'checkBox_{val[0]}'].isChecked() == True):
                lang_choice_list.append(val[0])

        if (self.new_excel_groupBox.isChecked() == True):

            excelModul(self.new_excel_path, lang_choice_list, True)
        else:
            excelModul(self.set_excel_path, lang_choice_list, False)

        lang_choice_list.clear()

        self.close()

    @AutomationFunctionDecorator
    def func_cencel(self, litter):
        self.close()

    # 0726
    def closeEvent(self, litter) -> None:
        self.mainwin.setDisabled(False)

    # 0725
    def keyPressEvent(self, a0: QKeyEvent) -> None:
        
        KEY_ENTER = 16777220

        print (f"a0.key() : {a0.key()}")
        if a0.key() == KEY_ENTER:
            self.func_check()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
