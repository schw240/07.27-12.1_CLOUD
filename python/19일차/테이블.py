import pymysql

def _create_area_table(db, cursor):
    sql = """
        CREATE TABLE Area (
        -- 지역명
        city_num VARCHAR(20) NOT NULL,
        city NVARCHAR(50)
    );
    """
    cursor.execute(sql)

def _create_gas_station_table(db, cursor):
    sql = """
        CREATE TABLE OilStations (
        -- 주유소명,휘발유가격,셀프주유소여부,등록일
        city_num VARCHAR(20) NOT NULL,
        gas_station_name NVARCHAR(50) NOT NULL,
        oil_price INT,
        is_self CHAR(1),
        reg_date DATETIME DEFAULT NOW()
    );
    """
    cursor.execute(sql)
