import os
import glob
import sqlite3
import traceback
from Log import LogManager
# from multiprocessing import Process, Lock

HDB = None

class DBManager:
    def __init__(self):
        if os.path.isdir('DataBase') != True:
            os.makedirs('DataBase')
        self.dbpath = "./DataBase/ExcelRPA.db"
        self.dbConn = sqlite3.connect(self.dbpath, isolation_level = None)
        self.c = self.dbConn.cursor()

    def close(self):
        self.dbConn.close()
        
    # def remove_db(self):
    #     self.close()
    #     os.remove(self.dbpath)
        
def find_db():
    file = glob.glob("./DataBase/ExcelRPA.db")
    if file != []:
        return True
    else:
        return False

def remove_db():
    os.remove("./DataBase/ExcelRPA.db")

def db_edit(cmd: str):
    HDB = DBManager()
    HDB.c.execute(cmd)
    HDB.close()

def db_insert(args1:str, args2:tuple):
    HDB = DBManager()
    HDB.c.execute(args1, args2)
    HDB.close()

def db_select(cmd: str):
    HDB = DBManager()
    HDB.c.execute(cmd)
    result = HDB.c.fetchall()
    HDB.close()
    return result

def db_tables(cmd: str):
    HDB = DBManager()
    HDB.c.execute(cmd)
    result = set([col_tuple[0] for col_tuple in HDB.c.description])
    HDB.close()
    return result
    
# def db_select(cmd: str):
#     HDB = DBManager()
#     try:
#         HDB.c.execute(cmd)
#     except:
#         msg = traceback.format_exc()
#         LogManager.HLOG.error(msg)
#         HDB.close()
#     HDB.close()

# lock = Lock()
# th_db = Process(target= db_control, args=(lock,))

if __name__ == "__main__":
    db = DBManager()
    db.close()