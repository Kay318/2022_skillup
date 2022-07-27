import os
import sqlite3

class DBManager:
    def __init__(self):
        self.dbpath = f"{os.getcwd()}\\ExcelRPA.db"
        self.dbConn = sqlite3.connect(self.dbpath)
        self.c = self.dbConn.cursor()
        self.__create_table()

    def close(self):
        self.dbConn.close()

    def __create_table(self):
        self.dbConn.executescript(
                """
                CREATE TABLE IF NOT EXISTS "Setup_Language" (
                    "언어" TEXT,
                    "경로" TEXT
                    );

                CREATE TABLE IF NOT EXISTS "Setup_Field" (
                    "Excel_Field" TEXT
                    );

                CREATE TABLE IF NOT EXISTS "Test_List" (
                    "평가목록" TEXT
                    );
                """
            )

    def create_target(self, TEXT):
        self.dbConn.executescript(
            TEXT
        )

if __name__ == "__main__":
    db = DBManager()
    db.close()