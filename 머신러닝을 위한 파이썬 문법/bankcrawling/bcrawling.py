import time
from selenium import webdriver
from bankclass import Bank


def RunCrawlingMyBank(driver):

	urls = list()
	nations = list()
	starting_url = 'https://www.mibank.me/exchange/saving/index.php'
	driver.get(starting_url)
	time.sleep(2)
	#페이지 진입

	for li in driver.find_elements_by_xpath('//*[@class="left_menu"]/ul'):
		lis = li.find_elements_by_xpath('.//li')
		#lis에서 li를 또 하나씩 가져와서 nation을 뽑고 nations에 append해야함
		for li in lis:
			nation = li.find_element_by_xpath('.//a').get_attribute('href').split('=')[1]
			nations.append(nation)
			time.sleep(1)
		print(nations)
	
	f = open('국가명.txt', 'w')
	for nation in nations:
		f.write(nation)
		f.write(',')
	f.close()



def crawling_each_bank(driver, nations):
	nation = nations
	
	for i in range(len(nation)):
		driver.get('https://www.mibank.me/exchange/saving/index.php?currency={0}'.format(nation[i]))
		time.sleep(2)
		sido_code = 2
		sido = driver.find_element_by_css_selector('#sido_code')
		#print(sido.text)
		sido.click()
		time.sleep(2)
		ggd = driver.find_element_by_css_selector('#sido_code > option:nth-child(4)')
		ggd.click()
		time.sleep(2)
		ok_btn = driver.find_element_by_xpath('//*[@id="search_form"]/div/a')
		ok_btn.click()
		time.sleep(2)
		#------------------------- 여기까지가 인천으로 바꾸고 확인까지 완료-------------------------------------
		#이 뒤부터 환율 실시간 크롤링 하면 됌



    			

		#boxcontents1까지 들어와야함 그리고 table을 다 가져와야함
		#재웅쌤 영화크롤링 코드 잠조

	# nation =['']
	# driver.get(url)
	# 'https://www.mibank.me/exchange/saving/index.php?currency={0}'.format(nation)

	#반복
	#1. 나라 주소로 딱 들어온다. - 전체나라
	#2. 지역을 서울 말고 다른곳 원하는곳으로 아무거나 바꾼후 확인
	#3. 정보 크롤링(스크래핑)

