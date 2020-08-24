import pymysql
from 등록 import _insert_oilstation, _insert_area
from 검색 import _search_oilstation, _search_cheap10
from 테이블 import _create_area_table, _create_gas_station_table
#from 크롤링 import _crawling
#from selenium import webdriver

db=pymysql.connect(host='localhost',port=3306,user='study',passwd='gkswnsla75!@',db='study',charset='utf8')
cursor = db.cursor()
#driver = webdriver.Chrome('C:/python/07.27-12.1_CLOUD/python/chromedriver.exe')


command = ''
while True:
    command = input('[메인메뉴] (1)지역등록, (2) 주유소등록, (3) 주유소검색, (4) 크롤링, (5) 테이블생성, (0) 종료\n원하는 명령을 입력해주세요:')
    if command == '1':
        print("지역등록")
        _insert_area(db, cursor)
    elif command == '2':
        print("주유소등록")
        _insert_oilstation(db, cursor)
    elif command == '3':
        print("주유소검색")
        sub_command = ''
        while True:
            sub_command = input('[주유소검색] (1)주유소명검색, (2)저렴한주유소(TOP10), (0)이전메뉴로')
            if sub_command == '1':
                print('주유소명 검색')
                name = input('검색하고싶은 주유소 이름을 입력하세요: ')
                _search_oilstation(db, cursor, name)
            elif sub_command == '2':
                print('저렴한 주유소 TOP 10')
                _search_cheap10(db, cursor)
            elif sub_command == '0':
                print('이전메뉴로 돌아갑니다.')
                break
    elif command == '4':
        print("크롤링")
        #_crawling(driver)
    elif command == '5':
        print('테이블 생성')
        _create_area_table(db, cursor)
        _create_gas_station_table(db, cursor)
    elif command == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령입니다. 다시 입력해주세요")
