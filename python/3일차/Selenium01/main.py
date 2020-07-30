from selenium import webdriver
from model_movie import Movie

driver = webdriver.Chrome()
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

table = driver.find_element_by_xpath('//*[@id="old_content"]/table')
trs = table.find_elements_by_xpath('.//tr') #테이블 안에서 찾겠다. 테이블 안에있는 tr을 모두 가지고 옴

movies = list()

#tds = table.find_elements_by_xpath('//td')
for tr in trs:
    tds = tr.find_elements_by_xpath('.//td')

    if len(tds) == 0 or len(tds) == 1:
        continue

    img = tds[0].find_element_by_xpath('.//img')
    alt = img.get_attribute('alt')    

    rank = int(alt)

    title = tds[1].text
    #print(title)

    movie = Movie(title, rank)
    movies.append(movie)

driver.quit()

f = open('c:/07.27-12.1_CLOUD/python/movielist.txt', 'w', encoding='utf8')
for m in movies:
    f.write('{0}위: {1}\n'.format(m.rank, m.title))
for m in movies:
    print(m.rank, m.title)

#//*[@id="old_content"]/table
#xpath는 html에서의 위치 
#xpath를 통해 셀레니움이 드라이버에서 알아서 찾아서 찾아감
