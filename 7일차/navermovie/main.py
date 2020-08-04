from selenium import webdriver
from p_naver import SeleniumMovie, SeleniumStaff, SeleniumMovieDetail
from adp_movie import SearchMovie


driver = webdriver.Chrome("C:/07.27-12.1_CLOUD/python/7일차/navermovie/chromedriver.exe")
# driver.get('https://nid.naver.com/nidlogin.login')
# driver.implicitly_wait(3)

# driver.find_element_by_name('id').send_keys('schw240')
# driver.implicitly_wait(3)
# driver.find_element_by_name('pw').send_keys('hippo123')
# driver.implicitly_wait(3)
# # 로그인 버튼을 클릭합니다
# login_btn = driver.find_element_by_id('log.login')
# login_btn.click()

command = ''

while command.upper() != 'EXIT':
    command = input('명령을 입력해주세요: ')

    #영화
    if command == '1':
        SeleniumMovie(driver)

    elif command == '2':
        movies = SearchMovie()
        count = 1
        for m in movies:
            m.show(count)
            count += 1

            SeleniumStaff(m, driver)
            
        