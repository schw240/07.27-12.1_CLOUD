import pymysql
import datetime

def _insert_oilstation(db , cursor):
    city_num = input('지역번호를 입력하세요: ')
    gas_station_name = input("주유소 이름을 입력하세요: ")
    oil_price = int(input('가격을 입력하세요: '))
    is_self = input('셀프 주유 여부를 입력하세요 Y or N: ')
    now_date = datetime.datetime.now()
    now_date + datetime.timedelta(days=5)

    reg_date = now_date.strftime("%Y%m%d")
    sql = """
        INSERT INTO oilstations (city_num,gas_station_name, oil_price, is_self, reg_date)
        VALUES(%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (city_num, gas_station_name, oil_price, is_self, reg_date))
    db.commit()

def _insert_area(db, cursor):
    city_num = input('지역 번호를 입력하세요: ')
    city = input("지역명을 입력하세요: ")
    sql = "INSERT INTO area (city_num, city) VALUES(%s, %s)"
    cursor.execute(sql, (city_num, city))
    db.commit()