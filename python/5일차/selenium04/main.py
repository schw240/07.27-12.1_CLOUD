from company import LoadCompany
from down import Download
from selenium import webdriver
import time
from read import CreateHtml
from find import Find
from stock import CreateStockHtml


driver = webdriver.Chrome()
comps = LoadCompany()
CreateStockHtml(comps)

for comp in comps:
    print(comp.symbol)
    print('<<{0} ({1}) 데이터 수집 시작>> '.format(comp.symbol, comp.name))
    Download(driver, comp.symbol)
    time.sleep(10)
    CreateHtml(comp.symbol)

command = ''
while command.upper() != 'EXIT':
   want = input("원하는 회사 코드를 입력하세요(종료를 원할 시 EXIT 입력): ")
   Find(want)