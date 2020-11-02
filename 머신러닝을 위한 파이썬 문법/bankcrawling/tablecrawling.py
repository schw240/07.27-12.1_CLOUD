import time
from selenium import webdriver
import datetime


bank_code = {'023':'StandardChartered', '020': '우리은행', '088': '신한은행', '003': '기업은행', '005': 'KEB하나', '031': '대구은행',
             '011': '농협은행', '032': '부산은행', '004': '국민은행', '035': '제주은행', '039': '경남은행', '007': '수협은행', '027': 'citibank',
             '037': '전북은행'}


driver = webdriver.Chrome('C:/Users/ASIA_03/BankProject/bankcrawling/chromedriver')
time.sleep(2)

driver.get('https://www.mibank.me/exchange/saving/index.php?currency=CNY')
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


table = driver.find_element_by_class_name('box_contents1')

# 환율만 크롤링할랭

tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
name = []
currency = []
saving = []
save_rating = []
today = []
i = 1
for index, value in enumerate(rows):
    for i in range(1, 6):
        body = value.find_elements_by_tag_name("td")[i]
        if i == 1:   # 1번 은행을 가져옴
            #코드 안에 있으면 해당 은행 이름으로 지정해주기
            
            bank_name_code = bank_code.find_element_by_xpath('.//a').get_attribute('href').split('=')[1] # 여기부터 막혀용
            #해당 코드 확인해서 집어넣기
            for code in bank_code:
                if bank_name_code == code[0]:
                    name.append(code[1])

            name.append(body)
        elif i == 2:
            currency.append(body)
        elif i == 3:
            saving.append(body)
        elif i == 4:
            save_rating.append(body)
        elif i == 5:
            today.append(body)
for i in range(len(name)):
    print(name[i].text)
for i in range(len(currency)):
    print(currency[i].text)
for i in range(len(saving)):
    print(saving[i].text)
for i in range(len(save_rating)):
    print(save_rating[i].text)
for i in range(len(today)):
    print(today[i].text)