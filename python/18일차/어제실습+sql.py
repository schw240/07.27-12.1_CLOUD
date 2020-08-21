import pymysql

db=pymysql.connect(host='localhost',port=3306,user='study',passwd='gkswnsla75!@',db='study',charset='utf8')
cursor = db.cursor()

def _insert(db, cursor):
    name = input("이름을 입력하세요: ")
    math = int(input("수학 점수를 입력하세요: "))
    english = int(input("영어 점수를 입력하세요: "))
    science = int(input("과학 점수를 입력하세요: "))
    sql = """
        INSERT INTO Grades (name, math, english, science)
        VALUES (%s, %s,%s,%s)
    """
    cursor.execute(sql,(name, math, english, science))
    db.commit()

def _search(db, cursor):
    sql = """
        SELECT *    
            FROM Grades
    """
    cursor.execute(sql)
    rs = cursor.fetchall()
    #print(type(rs))
    for cnt, i in enumerate(rs):
        print("순번: {4} 이름: {0}  수학: {1}  영어: {2}  과학: {3}".format(i[0], i[1], i[2], i[3],cnt ))
    

def _delete(db, cursor, num):
    sql = """
        DELETE FROM Grades
            WHERE seq = %s
    """
    cursor.execute(sql, num)
    db.commit()
    

command = ''
while True:
    command = input("명령을 입력해주세요!: 1 - 입력, 2 - 조회, 3 - 삭제, 0 - 종료 ")
    if command == '1':
        print("데이터베이스에 입력합니다.")
        _insert(db, cursor)
    elif command == '2':
        print("데이터베이스를 조회합니다.")
        _search(db, cursor)
    elif command == '3':
        print("데이터를 삭제합니다.")
        _search(db, cursor)
        num = int(input('삭제하고싶은 번호를 입력해주세요: '))
        _delete(db, cursor, num)
    elif command == '0':
        print('종료합니다.')
        break
