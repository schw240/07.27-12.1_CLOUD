# def _crawling(driver):
#     # 지역 - 서울 
#     url = 'http://www.opinet.co.kr/searRgSelect.do'
#     driver.get(url)
#     find_but = driver.find_element_by_xpath('//*[@id="header"]/div/ul/li[1]').click()
from selenium import webdriver
import time
driver = webdriver.Chrome('C:/python/07.27-12.1_CLOUD/python/chromedriver.exe')


url = 'http://www.opinet.co.kr/'
driver.get(url)
time.sleep(2)
url = 'http://www.opinet.co.kr/searRgSelect.do'
driver.get(url)

find_place = driver.find_element_by_xpath('//*[@id="SIDO_NM0"]').click()
select_seoul = driver.find_element_by_xpath('//*[@id="SIDO_NM0"]/option[2]').click()
find_sigu = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]').click()
# 여기서 반복으로 구를 바꿔가면서 검색
select_sigu = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]/option[2]').click()
_search = driver.find_element_by_xpath('//*[@id="searRgSelect"]').click()
#주유소명 휘발유        데이터베이스 지역번호 주유소명 가격 셀프여부 등록일
#tbody를 가져와 tr들을 받아옴
trs = driver.find_elements_by_xpath('//*[@id="body1"]/tr')
for tr in trs:
    tds = tr.find_elements_by_xpath('.//td').text

    #oilstation_name = tds.find_element_by_xpath('//*[@id="body1"]/tr[1]/td[1]/a').text
    #oil_price =  tds[2]
    #print(oilstation_name, oil_price)
time.sleep(1000)