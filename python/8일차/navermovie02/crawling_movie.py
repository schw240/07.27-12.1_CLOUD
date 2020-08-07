import time
from adp_movie import InsertMovie, ExistsMovie

def CrawlingMovie(driver):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200804&page={0}'
    page = 1

    isExists = True
    movie_code_list = list()

    while isExists == True:
        driver.get(url.format(page))
        trs = driver.find_elements_by_xpath('//*[@id="old_content"]/table/tbody/tr')
        
        for tr in trs:
            tds = tr.find_elements_by_xpath('.//td')
            if len(tds) == 1:
                continue

            href = tds[1].find_element_by_xpath('.//div/a').get_attribute('href')
            movie_code = href.split('=')[1]
            #print(movie_code)
            movie_code_list.append(movie_code)

        for m_code in movie_code_list:
            isExistsMovie = ExistsMovie(m_code)
            if isExistsMovie == True:
                continue

            movie_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={0}'
            driver.get(movie_url.format(m_code))
            time.sleep(2)
            dds = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd')

            _rating = ''
            if len(dds) == 3:
                _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[3]/p').text
            else :
                _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[4]/p').text

            _code = movie_code
            _title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3').text
            _title = _title.replace('상영중', '').replace('\n', '')
            try: 
                _story = driver.find_element_by_xpath('//*[@class="h_tx_story"]').text
            except:
                _story = driver.find_element_by_xpath('//*[@class="con_tx"]').text
            _genre = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
            try:
                _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[4]/p').text
            except:
                pass
            spans = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span')
            _open_date = ''
            if len(spans) == 4:
                _run_time = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]').text
                _open_date = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[4]').text
            elif len(spans) == 3:        
                _run_time = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[2]').text
                _genre = ''
                _open_date = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]').text
            _casting_count_url = 'https://movie.naver.com/movie/bi/mi/detail.nhn?code={0}'
            driver.get(movie_url.format(m_code))
            _casting_count = len(driver.find_elements_by_xpath('//*[@class="lst_people"]/li'))
            _image = driver.find_element_by_xpath('//*[@class="poster"]/a/img').get_attribute('src')
            

            InsertMovie(m_code, _title, _story, _genre, _rating, _run_time, _open_date, _casting_count, _image)
        page += 1
