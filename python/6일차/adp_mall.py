import pymssql
from model_pop_mall import Pop_mall


ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NOTEBOOK'
mall_list = list()

def SearchMall():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    #print(conn)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM POP_MALL')
    row = cursor.fetchone()
    mall_list.clear()

    while row:
        rank = row[0]
        date = row[1]
        name = row[2]

        mall = Pop_mall(rank, date, name)
        mall_list.append(mall)
        row = cursor.fetchone()

    return mall_list