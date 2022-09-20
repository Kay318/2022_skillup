import configparser

class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()
        

    def read_ini__test(self, table):
        """
        self.__read_ini__test() : ['Test_List']

        """
        self.config.read('Setup.ini', encoding='utf-8')

        get_List = []
        for i in self.config[table].values():
            get_List.append(i)

        return get_List
        
        
    def with_ini_test(self, val):
        self.config['Test_List'] = {}
        topsecret = self.config['Test_List']
        for i in range(0, len(val)):
            topsecret.setdefault(str(i + 1), val[i])

        with open("setup.ini", "w") as f:
            self.config.write(f)