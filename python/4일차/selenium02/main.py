from selenium import webdriver
from model_nation import Nation
import os

driver = webdriver.Chrome()
driver.get("file:///C:/python/4%EC%9D%BC%EC%B0%A8/htmtablel01/index.html")

table = driver.find_element_by_xpath('//table') #맨 처음에만 .을 찍을 필요가 없음
tr_list = table.find_elements_by_xpath('.//tr') #.을 찍으면 위의 테이블 안에서만 찾겠다는 의미 .을 안찍으면 만약에 테이블이 여러개인 경우 모든 테이블에서 tr을 가져오게 됨

nation_list = list()

for tr in tr_list:
    td_list = tr.find_elements_by_xpath('.//td')
    #print((len(td_list)))

    td_length = len(td_list)

    if td_length == 0:
        continue
    if td_length == 1:
        continue


    #국가
    nation = td_list[2].text
    #순서
    num = int(td_list[0].text)
    #수도
    capital = td_list[3].text
    #비고(인구수)
    population = int(td_list[4].text.replace(',',"")) #replace를 이용하여 인구에서 , 콤마 제거


    n = Nation(num, nation, capital , population) #클래스를 이용해 n이라는 인스턴스 생성
    
    nation_list.append(n) #만들어진 인스턴스를 리스트에 넣어줌
    #nation_list.append(Nation(num, nation, capital, population)) 이런 방식으로도 작성하는것이 가능함


print("<<가져온 데이터 총 {0}건>>".format(len(nation_list)))

for nat in nation_list:
    print(nat.num, nat.nation, nat.capital, nat.population)

#파일 쓰기
f = open('c:/07.27-12.1_CLOUD/python/4일차/nat_list.txt', 'w', encoding='utf8')
for nat in nation_list:
    line = nat.SaveLine()
    f.write(line)
f.close()

path = 'c:/python/4일차'
os.startfile(path)


driver.quit()
