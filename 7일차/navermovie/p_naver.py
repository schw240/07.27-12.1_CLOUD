import time
from adp_movie import InsertMovie, ExistsMovie
from adp_staff import InsertStaff, ExistsStaff


def SeleniumMovieDetail(m_code, driver):

    isExistsMovie = ExistsMovie(m_code)

    if isExistsMovie == True:
        return

    d_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={0}'
    driver.get(d_url.format(m_code)) #이렇게 해서 무비코드를 계속 가져와 다음 영화로 넘어감
    dds = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd')

    _rating = ''
    if len(dds) == 3:
        _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[3]/p').text
    else :
        _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[4]/p').text

    _code = m_code
    _title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3').text
    try: 
        _story = driver.find_element_by_xpath('//*[@class="h_tx_story"]').text
    except:
        _story = driver.find_element_by_xpath('//*[@class="con_tx"]').text
        
    _genre = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
    try:
        _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[4]/p').text
    except:
        _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[3]').text

    spans = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span')
    _open_date = ''
    if len(spans) == 4:
        _run_time = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]').text
        _open_date = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[4]').text
    elif len(spans) == 3:        
        _run_time = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[2]').text
        _genre = ''
        _open_date = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]').text




    InsertMovie(_code, _title, _story, _genre, _rating, _run_time, _open_date)
    #time.sleep(5)


def SeleniumMovie(driver):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200803&page={0}'
    page = 1

    isExists = True
    m_codes_list = list()
    while isExists == True:
        
        driver.get(url.format(page))
        trs = driver.find_elements_by_xpath('//*[@id="old_content"]/table/tbody/tr')

        for tr in trs:
            tds = tr.find_elements_by_xpath('.//td')
            if len(tds) == 1:
                continue

            #/movie/bi/mi/basic.nhn?code=17153 영화 코드 구하기
            href = tds[1].find_element_by_xpath('.//div/a').get_attribute('href')
            m_code = href.split('=')[1] #split을 이용하여 href를 '=' 앞 뒤로 나누었을 때 '='의 뒤에있는 것이 무비 코드이므로 [1]로 가져옴
            m_codes_list.append(m_code)

        for code in m_codes_list:
            SeleniumMovieDetail(code, driver)

    
        page += 1


def SeleniumStaff(movie, driver):
    d_url = 'https://movie.naver.com/movie/bi/mi/detail.nhn?code={0}'
    driver.get(d_url.format(movie.code))

    #펼쳐보기
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="actorMore"]').click()
    except:
        pass

    act_lis = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[2]/ul/li')

    for act in act_lis:
        href = act.find_element_by_xpath('.//*[@class="p_info"]/a').get_attribute('href')
        _s_code = href.split('=')[1]
        _k_name = act.find_element_by_xpath('.//*[@class="k_name"]').text
        _e_name = act.find_element_by_xpath('.//*[@class="e_name"]').text
        try:
            _cast_name = act.find_element_by_xpath('.//*[@class="pe_cmt"]').text
        except:
            pass
        _role_info = act.find_element_by_xpath('.//*[@class="p_part"]').text
        _birth = ''
        _nation = ''
        _is_director = Falsess
        _is_actor = True

        isExists = ExistsStaff(_s_code)

        if isExists == False:
            InsertStaff(_s_code, _k_name, _e_name, _cast_name, _role_info, _birth, _nation, _is_director, _is_actor)


    time.sleep(10)

