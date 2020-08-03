import pymssql
from model_company import Company


ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NOTEBOOK'
company_list = list()

def SearchCP():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM COMPANY')
    row = cursor.fetchone()
    print(row, type(row))
    company_list.clear()

    while row:
        search = row[0]
        brand = row[1]
        date = row[2]
        rank = row[3]
        nation = row[4]

        cp = Company(search, brand, date, rank, nation)
        company_list.append(cp)
        row = cursor.fetchone()

    return company_list