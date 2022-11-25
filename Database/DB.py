import os
import glob
import sqlite3

class DBManager:
    def __init__(self):
        if os.path.isdir('DataBase') != True:
            os.makedirs('DataBase')
        self.dbpath = "./DataBase/ExcelRPA.db"
        self.dbConn = sqlite3.connect(self.dbpath)
        self.c = self.dbConn.cursor()

    def close(self):
        self.dbConn.close()
        
    def __del__(self):
        self.dbConn.close()        

    def create_target(self, TEXT):
        self.dbConn.executescript(
            TEXT
        )
        
    def remove_db(self):
        self.close()
        os.remove(self.dbpath)
        
    def find_db(self):
        file = glob.glob(self.dbpath)
        if file != []:
            return True
        else:
            return False

if __name__ == "__main__":
    db = DBManager()
    db.close()