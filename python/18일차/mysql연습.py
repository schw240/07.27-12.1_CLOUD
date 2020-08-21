import pymysql

db=pymysql.connect(host='localhost',port=3306,user='study',passwd='gkswnsla75!@',db='study',charset='utf8')

cursor=db.cursor()


sql = """
    SELECT *
        FROM Grades2
"""

cursor.execute(sql)
rs = cursor.fetchall()


for i in rs:
    print("이름: {0}".format(i[0]))