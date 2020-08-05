import pymssql
from model_movie import Movie

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def ExistsMovie(_code):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM MOVIE_LIST WHERE CODE = %s'
    cursor.execute(query, _code)

    isExists = False
    row = cursor.fetchone()

    while row:
        isExists = True
        break

    return isExists

def InsertMovie(_code, _title, _story, _genre, _rating, _run_time, _open_date, _casting_count):

    openDates = _open_date.split(',')

    if len(openDates) > 1:
        _open_date = openDates[-1]

    _run_time = _run_time.replace('분', '')
    _open_date = _open_date.replace(' ', '').replace('개봉', '').replace('.', '-').replace('재개봉,', '')
    
    if len(_open_date) == 7:
        _open_date += '-01'

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()

    query = '''
        INSERT MOVIE_LIST(CODE, TITLE, STORY, GENRE, RATING, RUN_TIME, OPEN_DATE, CASTING_COUNT)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
        '''    
    cursor.execute(query, (_code, _title, _story, _genre, _rating, _run_time, _open_date, _casting_count))
    conn.commit()




def SearchMovie():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT * FROM MOVIE_LIST'
    cursor.execute(query)

    movie_list = list()
    row = cursor.fetchone()

    while row:
        _code = row[0]
        _title = row[1]
        _story = row[2]
        _genre = row[3]
        _rating = row[4]
        _run_time = row[5]
        _open_date = row[6]
        _casting_count = row[7]

        m = Movie(_code, _title, _story, _genre, _rating, _run_time, _open_date, _casting_count)

        movie_list.append(m)
    
        print(m.code, m.title, m.story, m.genre, m.rating, m.run_time, m.open_date, m.casting_count)

        row = cursor.fetchone()
        

    return movie_list
