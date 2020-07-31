from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.saramin.co.kr/zf_user/jobs/list/job-category')

btn_it = driver.find_element_by_xpath('//*[@id="sri_lnb"]/ul/li[1]/ul/li[3]/a').click()
time.sleep(2)

btn_category = driver.find_element_by_xpath('//*[@id="depth2_btn_404"]').click()
time.sleep(2)

btn_python = driver.find_element_by_xpath('//*[@id="sp_job_category_lastDepth_404"]/li[12]/div/label').click()
time.sleep(2)

btn_search = driver.find_element_by_xpath('//*[@id="search_btn"]').click()
time.sleep(2)

btn_place = driver.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/ul/li[2]').click()
time.sleep(2)

btn_seoul = driver.find_element_by_xpath('//*[@id="depth1_btn_101000"]').click()
time.sleep(2)
btn_gg = driver.find_element_by_xpath('//*[@id="depth1_btn_102000"]').click()
time.sleep(2)

btn_search = driver.find_element_by_xpath('//*[@id="search_btn"]').click()
time.sleep(2)

btn_career = driver.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]').click()
time.sleep(2)
btn_newbie = driver.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]').click()
time.sleep(2) 

btn_search = driver.find_element_by_xpath('//*[@id="search_btn"]').click()
time.sleep(2)

btn_pangyo = driver.find_element_by_xpath('//*[@id="async_sfilter"]/div/div[2]/div[2]/ul/li[1]/input').click()
########################################
#시나리오
#1. list_body 의 div들을 전부 읽음
#2. 각 div안에서 company_nm, notification_info, recruit_condition(p class 안에 career, education), company_info(p class 안에 employment_type, work_place), support_info(deadline))

list_body = driver.find_element_by_xpath('//*[@id="default_list_wrap"]/section/div[2]') #list_body를 받아 list안에 들어있는 div들을 읽을거임
print(list_body)
div_company_nm = list_body.find_element_by_xpath('//*[@id="rec-38496131"]/div[2]')
print(div_company_nm)
company_nm = div_company_nm.find_element_by_xpath('.//*[@class="col notification_info"]')
print(company_nm)