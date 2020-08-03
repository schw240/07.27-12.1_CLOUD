import pymssql
from model_notebook import Notebook


ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NOTEBOOK'
nb_list = list()

def SearchNB():
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM NB_LIST')
    
    row = cursor.fetchone()
    nb_list.clear()

    while row:
        brand = row[0]
        name = row[1]
        date = row[2]
        rank = row[3]
        low_price = row[4]
        seller = row[5]
        gpa = row[6]

        nb = Notebook(brand, name, date, rank, low_price, seller, gpa)
        nb_list.append(nb)
        row = cursor.fetchone()

    return nb_list