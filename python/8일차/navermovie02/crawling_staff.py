import pymssql
from adp_staff import InsertStaff, ExistStaff
from adp_casting import InsertCasting, ExistsCasting
from adp_movie import ExistsMovie
import time

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def CrawlingStaff(driver):
    #데이터베이스에서 확movie_list 확인하여 movie_code를 가져옴
    #가져온 movie_code를 리스트에 저장
    #반복문을 통해 movie_code를 가져와 한 페이지씩 들어가 배우/제작진 버튼을 클릭 후 정보 가져오기
    movie_code_list = list()
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM MOVIE_LIST'
    cursor.execute(query)

    row = cursor.fetchone()
    while row:
        movie_code_list.append(row[0])
        isExistsMovie = ExistsMovie(row[0])
        if isExistsMovie == True:
            row = cursor.fetchone()
    
    # movie_code_list에 현재 저장된 영화의 CODE모두 저장됨
    #해당 CODE를 가지고 영화페이지로 계속 이동하면서 제작진 정보 가져올거임
    movie_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={0}'
    for code in movie_code_list:
        driver.get(movie_url.format(code))
        #중복체크도 필요
        #배우/제작진 버튼 클릭
        driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[2]').click()
        #펼쳐보기
        time.sleep(2)
        try:
            driver.find_element_by_xpath('//*[@id="actorMore"]').click()
        except:
            pass

        lis = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[2]/ul/li')
        _nation = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[2]/a').text
        #배우
        for li in lis:
            staff_href = li.find_element_by_xpath('.//p/a').get_attribute('href')
            staff_code = staff_href.split('=')[1]
            _k_name = li.find_element_by_xpath('.//*[@class="k_name"]').text
            try:
                _cast_name = li.find_element_by_xpath('.//*[@class="pe_cmt"]').text
            except:
                _cast_name = '조연'
            isExistsStaff = ExistStaff(staff_code)
            if isExistsStaff == False:
                InsertStaff(staff_code, _k_name, _nation, False)
                InsertCasting(code, staff_code, _cast_name, False)