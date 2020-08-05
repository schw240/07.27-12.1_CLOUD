import pymssql
from model_casting import Casting

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def ExistsCasting(_staff_code):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT STAFF_CODE FROM CASTING_LIST WHERE STAFF_CODE = %s'

    cursor.execute(query, _staff_code)

    isExists = False
    row = cursor.fetchone()

    while row:
        isExists = True
        break

    return isExists

def InsertCasting(_movie_code, _staff_code, _cast_name, _is_director):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = '''
        INSERT CASTING_LIST(MOVIE_CODE, STAFF_CODE, CAST_NAME, IS_DIRECTOR)
        VALUES(%s, %s, %s, %s)
        '''    
    cursor.execute(query, (_movie_code, _staff_code, _cast_name, _is_director))
    conn.commit()

def SearchCasting():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT * FROM CASTING_LIST'
    cursor.execute(query)

    casting_list = list()
    row = cursor.fetchone()

    while row:
        _movie_code = row[0]
        _staff_code = row[1]
        _cast_name = row[2]
        _is_director = row[3]

        ct = Casting(_movie_code, _staff_code , _cast_name, _is_director)

        casting_list.append(ct)
        print(ct.movie_code, ct.staff_code, ct.cast_name, ct.is_director)

        row = cursor.fetchone()

    return casting_list