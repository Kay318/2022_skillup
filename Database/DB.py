import os
import sqlite3

class DBManager:
    def __init__(self):
        self.dbpath = f"{os.getcwd()}\\ExcelRPA.db"
        self.dbConn = sqlite3.connect(self.dbpath)
        self.__create_table()

    def __del__(self):
        self.dbConn.close()

    def __create_table(self):
        self.dbConn.executescript(
                """
                CREATE TABLE IF NOT EXISTS "Setup_Language" (
                    "언어" TEXT,
                    "경로" TEXT
                    );
                """
            )

if __name__ == "__main__":
    db = DBManager()
    db.close()