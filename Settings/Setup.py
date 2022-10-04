import configparser
from doctest import Example
from operator import index
from Log import LogManager as lm

class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def create_table(self, table):
        self.config[table] = {}
        with open("setup.ini", "w", encoding="utf-8") as f:
            self.config.write(f)

    def read_ini__test(self, table):
        """
        self.__read_ini__test() : ['Test_List']

        """
        self.config.read('Setup.ini', encoding='utf-8')

        key1 = None
        key2 = None
        val_List = []
        sub_List = []
        sec = self.config.sections()
        print(f"sec : {sec}")

        try:
            example = self.config[table]
            if (table == "Language"):
                key1 = "lang_key"
                key2 = "lang_path"
            elif (table == "Field"):
                key1 = "field_key"
            elif (table == "Test_List"):
                key1 = "testlist_key"
            
            for key in example.keys():
                if key.find(key1) != -1:
                    print(f'key1 : {key}')
                    val_List.append(example[key])
                elif key.find(key2) != -1:
                    print(f'key2 : {key}')
                    sub_List.append(example[key])
        except Exception as e:
            lm.Interupt()

        return val_List, sub_List
        
        
    """
    ~# PYTHONIOENCODING=UTF-8
    
    for 문 안에서 호출 필요
    table : table 명
    val : 저장할 값 1
    val2 : 저장할 값 2
    * table명을 제외한 나머지 key값들은 소문자로만 저장되면 인식된다.
    """
    def with_ini_test(self, table, count, val, val2):

        key = None
        key2 = None

        if (table == "Language"):
            key = "lang_key"
            key2 = "lang_path"
        elif (table == "Field"):
            key = "field_key"
        elif (table == "Test_List"):
            key = "testlist_key"

        self.config[table].setdefault(f'{key}_{count + 1}', val)

        if (val2 != None):
            self.config[table].setdefault(f'{key2}_{count + 1}', val2)

        return self.config

    def save_ini(self, save_key : configparser.ConfigParser()):
        with open("setup.ini", "w", encoding="utf-8") as f:
            save_key.write(f)