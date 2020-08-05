import pymssql
from model_staff import Staff

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def ExistStaff(_staff_code):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM STAFF_LIST WHERE CODE = %s'
    cursor.execute(query, _staff_code)

    isExists = False
    row = cursor.fetchone()
    while row:
        isExists = True
        break

    return isExists


def InsertStaff(_code, _k_name, _nation, _is_director):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = '''
        INSERT STAFF_LIST(CODE, K_NAME, NATION, IS_DIRECTOR)
        VALUES(%s, %s, %s, %s)
        '''
    cursor.execute(query, (_code, _k_name, _nation, _is_director))
    conn.commit()


def SearchStaff():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT * FROM STAFF_LIST'
    cursor.execute(query)

    staff_list = list()
    row = cursor.fetchone()

    while row:
        _code = row[0]
        _k_name = row[1]
        _nation = row[2]
        _is_director = row[3]

        sf = Staff(_code, _k_name, _nation, _is_director)

        staff_list.append(sf)
        print(sf.code, sf.k_name, sf.nation, sf.is_director)

        row = cursor.fetchone()

    return staff_list