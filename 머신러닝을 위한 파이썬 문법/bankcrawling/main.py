from selenium import webdriver
from bcrawling import RunCrawlingMyBank, crawling_each_bank
from search_nation import search_nation

command = ''

while command.upper() != 'EXIT':
    command = input('명령을 입력해주세요.')


    if command == '1': # 크롤링 뱅크 등록
        #나라 이름 가지고오기
        RunCrawlingMyBank(webdriver.Chrome())
    elif command == '2': #나라이름 조회하기
        nations = search_nation()
    elif command == '3': #각 나라별 은행, 환율, 절약금액, 절약율크롤링해오기
        crawling_each_bank(webdriver.Chrome(), nations)