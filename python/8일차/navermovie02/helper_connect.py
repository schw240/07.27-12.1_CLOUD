import pymssql

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def NewConnect():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    return conn