import pymssql

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER'

def ExistsStaff(_code):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM STAFF_LIST WHERE CODE = %s'
    cursor.execute(query, _code)

    isExists = False
    row = cursor.fetchone()
    while row:
        isExists = True
        break

    return isExists



def InsertStaff(_s_code, _k_name, _e_name, _cast_name, _role_info, _birth, _nation, _is_director, _is_actor):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = '''
            INSERT STAFF_LIST (CODE, K_NAME, E_NAME, BIRTH, NATION, IS_DIRECTOR, IS_ACTOR)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''

    cursor.execute(query, (_s_code, _k_name, _e_name, _birth, _nation, _is_director, _is_actor))
        
    conn.commit()
