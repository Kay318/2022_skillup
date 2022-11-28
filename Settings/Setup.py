import configparser
import traceback
from Log import LogManager

class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def create_table(self, table):
        self.config[table] = {}
        with open("./Settings/Setup.ini", "w", encoding="utf-8") as f:
            self.config.write(f)

    def read_setup(self, table): # updateList

        # def excel_result(key:object, data:object, val1_List:list):
        #     start_settings = ["이미지 가로 크기", "이미지 세로 크기", "이미지 셀 행 크기", "시트 셀 기본 열 크기", "시트 셀 기본 행 크기"]

        #     if key in start_settings:
        #             val1_List.append(data[key])
            
        #     return val1_List

        self.config[table] = {}
        self.config.read('./Settings/Setup.ini', encoding='utf-8')
        key1 = "None"
        key2 = "None"
        val1_List = []
        val2_List = []

        try:
            data = self.config[table]
            if (table == "Language"):
                key1 = "lang_key"
                key2 = "lang_path"
            elif (table == "Field"):
                key1 = "field_key"
            elif (table == "Test_List"):
                key1 = "testlist_key"
            elif (table == "Excel_Setting"):
                key1 = "excel_setting"
            
            for key in data.keys():
                if key.find(key1) != -1:
                    val1_List.append(data[key])
                elif key.find(key2) != -1:
                    val2_List.append(data[key])
                # elif table == "Excel_Setting":
                #     excel_result(key=key, data=data, val1_List=val1_List)

        except Exception as e:
            msg = traceback.format_exc()
            LogManager.HLOG.error(msg)

        return val1_List, val2_List
        
        
    """
    ~# PYTHONIOENCODING=UTF-8
    
    for 문 안에서 호출 필요
    table : table 명
    val : 저장할 값 1
    val2 : 저장할 값 2
    * table명을 제외한 나머지 key값들은 소문자로만 저장되면 인식된다.
    """
    def write_setup(self, table, count, val, val2): # updateList

        key = None
        key2 = None

        if (table == "Language"):
            key = "lang_key"
            key2 = "lang_path"
        elif (table == "Field"):
            key = "field_key"
        elif (table == "Test_List"):
            key = "testlist_key"
        elif (table == "Excel_Setting"):
            key = "excel_setting"

        # if (table == "Excel_Setting"):
        #     self.config[table].setdefault(f'{val}', val2)
        # else:
        self.config[table].setdefault(f'{key}_{count + 1}', val)

        if (val2 != None):
            self.config[table].setdefault(f'{key2}_{count + 1}', val2)

        self.save_ini()

    def clear_table(self, table):
        self.config[table].clear()
        self.save_ini()

    def save_ini(self):
        with open("./Settings/Setup.ini", "w", encoding="utf-8") as f:
            self.config.write(f)