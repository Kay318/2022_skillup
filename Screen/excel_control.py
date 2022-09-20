from csv import excel
from multiprocessing import active_children
from re import I
from typing import List
import openpyxl as xl
import xlwings as wings
import pandas
from openpyxl.drawing.image import Image
from Database.DB import DBManager

class excelModul(DBManager):
    
    def __init__(self, save_path, lang_List, new_set_difference) -> excel:
        super().__init__()
        self.start_column = 1
        self.lang_cnt = 1
        
        if (new_set_difference):

            wb = xl.Workbook()

            for lang in lang_List:

                active = wb.create_sheet(title=lang)

                # 초기세팅
                active.cell(row=1, # 현재 진행상황
                            column= self.lang_cnt, # 평가한 나라 개수 영향
                            value=lang)

                idx = self.start_column + self.lang_cnt # 언어 1개 고정
                for val in self.평가목록크기():
                    active.cell(row=1, # 현재 진행상황
                                column= idx, # 평가한 나라 개수 영향
                                value=val)
                    idx = idx + 1

                jdx = idx
                for val in self.평가필드크기():
                    active.cell(row=1, # 현재 진행상황
                                column= jdx, # 평가한 나라 개수 영향
                                value=val)
                    jdx = jdx + 1

                active.cell(row=1, # 현재 진행상황
                            column= jdx, # 평가한 나라 개수 영향
                            value="버전정보")

                # self.excel_data_input(active)

                print(f"save_path : {save_path}")

            wb.save(f'{save_path}\\excelTest.xlsx')

        else:
            # 기존 엑셀 생성
            debug.set_debug(save_path)
            try:
                print()
            except debug.Interupt:
                debug.Interupt.set_error() 
            wb = wings.Book(save_path)
            for lang in lang_List:
                sheet = wb.sheets[lang]
                for lang in sheet:
                    print(lang)
                

    def 이미지개수당셀생성(self) -> List:
        """
        1. DB 받아오기
        2. 저장된 DB중 이미지 경로 있는것만 구별시키기
        3. 이미지 개수를 확인하고 : return 해당경로를 순서대로 List 반환
        """

        self.c.execute('SELECT * FROM 평가결과저장된DB')
        dataList = self.c.fetchall()
        idx = 0 # "평가결과저장된데이터중 경로위치"
        img_pathList = []

        # 행마다 차래로
        for data in dataList:
            
            if data != "":
                # clume서치
                img_pathList.append(data[idx])

        return img_pathList

    def 평가개수당셀생성(self, row) -> List:
        """
        1. DB 받아오기
        2. 저장된 DB중 이미지 경로 있는것만 구별시키기
        3. 이미지 개수를 확인하고 : return 해당경로를 순서대로 List 반환
        """

        self.c.execute('SELECT * FROM 평가결과저장된DB')
        dataList = self.c.fetchall()
        idx = 0 # "평가결과저장된데이터중 경로위치"
        img_pathList = []

        for data in dataList[row]:
            
            if data != "":
                img_pathList.append(data)

        return img_pathList

    def 평가목록크기(self) -> List:
        self.c.execute(f"SELECT 평가목록 FROM Test_List")
        dataList = self.c.fetchall()
        result_cellList = []

        for data in dataList:
            
            if data != "":
                result_cellList.append(data[0])

        print(f"result_cellList {result_cellList}")
        return result_cellList


    def 평가필드크기(self) -> List:
        self.c.execute(f"SELECT * FROM Setup_Field")
        dataList = self.c.fetchall()
        result_cellList = []

        for data in dataList:
            
            if data != "":
                result_cellList.append(data[0])

        return result_cellList

    def excel_data_input(self, active):
        # 데이터 추가
                row_count = 2
                for path in self.이미지개수당셀생성():

                    img = Image(path)
                    active.add_image(img=img, anchor=active.cell(row = row_count, column = 1)) # 이미지 추가

                    pre = 0
                    
                    for idx in range(self.lang_cnt, len(self.평가목록크기()) + self.lang_cnt):

                        if (idx + self.lang_cnt <= len(self.평가목록크기()) + self.lang_cnt):
                            active.cell(row=row_count,
                                column= idx + self.lang_cnt,
                                value = self.평가개수당셀생성(row=row_count)[pre])
                            pre = pre + 1

                    # 라벨 평가 넣기
                    # 버전정보넣기

                    row_count = row_count + 1