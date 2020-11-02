import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/ASIA_03/BankProject/bankcrawling/chromedriver')
time.sleep(3)

table = driver.find_element_by_class_name('only_bank')

tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("span")


for index, value in enumerate(rows):
    body=value.find_elements_by_xpath('.//span[@class="sreader"]').get_attribute('textContent')
    print(body.text)

# //div[contains(@class,'panelMessage ')]//span[@class='amountCharged']

# day_lists = driver.find_elements_by_tag_name('li')
# for day_list in day_lists:
#     print(day_list.find_element_by_xpath('.//span[@class="sreader"]').get_attribute('textContent'))