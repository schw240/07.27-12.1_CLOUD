import time
from selenium import webdriver
from model_actor import Actor
from model_movie import Movie

driver = webdriver.Chrome()

isExistsPage = True
list_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200729&page={0}'
count = 0
while isExistsPage == True:
    count = count + 1
    #url 구하는 식
    driver.get(list_url.format(count))
    table = driver.find_element_by_xpath('//*[@id="old_content"]/table')
    tbody = table.find_element_by_xpath('.//tbody')
    trs = tbody.find_elements_by_xpath('.//tr')
    urls = list()


    for tr in trs:
        
        tds = tr.find_elements_by_xpath('.//td')

        if len(tds) == 1:
            continue

        div = tds[1].find_element_by_xpath('.//div')
        a = div.find_element_by_xpath('.//a')
        href = a.get_attribute('href')
        urls.append(href)
    ###################################################################################여기까지 url 구하는 식
    #순위대로 영화의 url로 이동
    # for url in urls:
    #     driver.get(url)
    #     time.sleep(5)   

    movies = list()

    for url in urls:
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[2]/a').click()
        title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a')
        nation = driver.find_element_by_xpath('//*[@class="info_spec"]/dd/p/span[2]')
        #print(title.text, nation.text)

        #배우가 많아서 펼쳐야 하는 경우
        try:
            driver.find_element_by_xpath('//*[@id="actorMore"]').click()
        except:
            pass

        lis = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[2]/ul/li')
        #lis = ul.find_elements_by_xpath('.//li')

        act_list = list()

        for li in lis:
            actname = li.find_element_by_xpath('.//*[@class="k_name"]').text
            ename = li.find_element_by_xpath('.//*[@class="e_name"]').text    
            p_part = li.find_element_by_xpath('.//*[@class="p_part"]').text

            pe_cmt = ''
            try:
                pe_cmt = li.find_element_by_xpath('.//*[@class="pe_cmt"]').text
            except:
                pe_cmt = '없음'
            #print(actname, ename, p_part, pe_cmt)
        
            act = Actor(actname, ename, p_part, pe_cmt)
            act_list.append(act)

    #print('제목: {0}\t제작국가: {1}'.format(title.text, nation.text))
    #for act in act_list:
    #    print('{0}: {1}  ({2})'.format(act.p_part, act.actname, act.ename))

    # 된사람들은 타이틀 , 네이션을 포함한 act_list를 (어벤져스의 한 세트이므로) 이것들을 한번에 아우를 수 있는 movie class를 만들어보세요

        mov = Movie(title.text, nation.text, act_list)
        movies.append(mov)

        print('완료: {0}, 배우: {1}명'.format(mov.title, len(mov.acts)))

    print('{0} 페이지 완료'.format(count))

    #print(mov.title, mov.nation, mov.acts[i].actname, mov.acts[i].ename, mov.acts[i].p_part, mov.acts[i].pe_cmt)

    # for act in mov.acts:
    #     print(act.actname, act.ename, act.p_part, act.pe_cmt)

