from selenium import webdriver
from adp_casting import SearchCasting, InsertCasting, ExistsCasting
from adp_movie import SearchMovie, InsertMovie, ExistsMovie, GetMovies
from adp_staff import SearchStaff, ExistStaff, InsertStaff
from crawling_movie import CrawlingMovie
from crawling_staff import CrawlingStaff
from create_html import CreateHtml
from generate_html import GenMovieDetailHtml, GenMovieHtml

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
        CrawlingMovie(driver)
    elif command == '5':
        CrawlingStaff(driver)
    elif command == '6':
        CreateHtml()
    if command == '7': # 영화목록 HTML 생성
        GenMovieHtml(GetMovies(), 'C:/07.27-12.1_CLOUD/python/8일차/navermovie02/html/movielist.html')
    if command == '8': # 영화목록 별 영화 상세페이지 HTML 생성
        GenMovieDetailHtml(GetMovies(), 'c:/python/moviedetail')
    else:
        print('잘못된 명령입니다.')
    
