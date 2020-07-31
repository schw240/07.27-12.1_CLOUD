import time
import shutil
from company import LoadCompany
from os import path


def Download(driver, code):
    
    url = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
    driver.get(url.format(code))
    time.sleep(1)

    isSelectClick = False
    while isSelectClick == False:
        try:
            select = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div').click()
            time.sleep(2)
            isSelectClick = True
        except:
            time.sleep(2)

    btn_max = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button').click()
    time.sleep(1)

    btn_apply = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()
    time.sleep(1)

    btn_down = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()
    ####################################################################################################################################### 다운로드 완료

    #다운로드 받은 파일 이동하기

    filename = '{0}.csv'.format(code)
    src = 'C:/Users/user/Downloads/{0}'.format(filename)
    dir = 'C:/07.27-12.1_CLOUD/python/finance/{0}'.format(filename)

    isExists = False
    while isExists != True:
        isExists = path.exists(src)
        time.sleep(1)


    shutil.move(src, dir)
