import pymysql

# 1.주유소명검색선택시검색어를사용자에게받고해당검색어를포함하는주유소출력
# 출력내용:주유소명,휘발유가격,셀프주유소여부,등록일
# 2.저렴한주유소(TOP10)선택시전체주유소중가장저렴한주유소10개를출력
# 출력내용:지역명,주유소명,휘발유가격,셀프주유소여부,등록일(조인필요)

def _search_oilstation(db, cursor, name):
    sql = """
        SELECT *
        FROM oilstations
        WHERE gas_station_name = %s
    """
    cursor.execute(sql, name)
    rs = cursor.fetchall()
    #print(rs)
    for i, item in enumerate(rs):
        if rs[i][1] == name:
            print(rs[i])
        else:
            continue

def _search_cheap10(db, cursor):
    sql = """
        SELECT area.city, oilstations.* 
        FROM area
        INNER JOIN oilstations
        ON area.city_num = oilstations.city_num
        ORDER BY oilstations.oil_price ASC
        LIMIT 10
    """
    cursor.execute(sql)
    rs = cursor.fetchall()
    cnt = 0
    for item in rs:
        cnt += 1
        print("{0}위: {1}".format(cnt, item))
        