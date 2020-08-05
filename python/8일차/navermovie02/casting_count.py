import pymssql

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def updateCastingCount():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'UPDATE MOVIE_LIST SET CASTING_COUNT={0} WHERE CASTING_COUNT=0';

    row = cursor.fetchone()

    while row:
        movie_code_list.append(row[0])
        print(row[0])
        row = cursor.fetchone()

    movie_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={0}'
    for code in movie_code_list:
        driver.get(movie_url.format(code))
        driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[2]').click()
        try:
            driver.find_element_by_xpath('//*[@id="actorMore"]').click()
        except:
            pass

        lis = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[2]/ul/li')
        cursor.execute(query.format(len(_casting_count)))
