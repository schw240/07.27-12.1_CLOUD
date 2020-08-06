from selenium import webdriver
from adp_casting import SearchCasting, InsertCasting, ExistsCasting
from adp_movie import SearchMovie, InsertMovie, ExistsMovie
from adp_staff import SearchStaff, ExistStaff, InsertStaff
from crawling_movie import CrawlingMovie
from crawling_staff import CrawlingStaff
from casting_count import updateCastingCount
from create_html import CreateHtml
import time

driver = webdriver.Chrome('C:/python/07.27-12.1_CLOUD/python/chromedriver.exe')

command = ''

while command.upper() != 'EXIT':
    command = input('명령을 입력해주세요: ')

    if command == '1':
        SearchMovie()
    elif command == '2':
        SearchStaff()
    elif command == '3':
        SearchCasting()
    elif command == '4':
        _code = 123456
        _title = 'a'
        _story = 'gg'
        _genre = 'sf'
        _rating = '전체'
        _run_time = 123
        _open_date = '2020-11-11'

        isExistsMovie = ExistsMovie(_code)
        if isExistsMovie == False:
            InsertMovie(_code, _title, _story, _genre, _rating, _run_time, _open_date)
        else:
            print('중복')
    elif command == '5':
        _code = 141515
        _k_name = '로버트다우니주니어'
        _nation = '미국'
        _is_director = False

        isExistsStaff = ExistStaff(_code)
        if isExistsStaff == False:
            InsertStaff(_code, _k_name, _nation, _is_director)
        else:
            print('중복')
    elif command == '6':
        _movie_code = 1231235
        _staff_code = 162462436
        _cast_name = '헐크'
        _is_director = False

        isExistsCasting = ExistsCasting(_staff_code)
        if isExistsCasting == False:
            InsertCasting(_movie_code, _staff_code, _cast_name, _is_director)
        else:
            print('중복')
    elif command == '7':
        CrawlingMovie(driver)
    
    elif command == '8':
        CrawlingStaff(driver)
    elif command == '9':
        updateCastingCount()
    elif command == '10':
        CreateHtml()
    
