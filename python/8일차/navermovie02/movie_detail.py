import pymssql

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'


def MovieDetail(movie_code):
    
    #링크를 타고가면 영화 상세 정보 페이지를 만들거임
    #네이버 영화 참조
    #타이틀 , 사진, 주요정보, 배우/제작진, 줄거리,
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = '''
            SELECT DISTINCT STAFF_LIST.CODE, STAFF_LIST.K_NAME, STAFF_LIST.NATION, CASTING_LIST.MOVIE_CODE, CASTING_LIST.CAST_NAME
            FROM CASTING_LIST, STAFF_LIST
            WHERE STAFF_LIST.CODE = CASTING_LIST.STAFF_CODE AND CASTING_LIST.MOVIE_CODE = %s
            ORDER BY CASTING_LIST.MOVIE_CODE
            '''
    #가지고 오는것
    # 0. 스태프 코드
    # 1. 스태프 이름
    # 2. 스태프 국적
    # 3. 영화 코드
    # 4. 배역 이름

    style_text = '''
            <style>
                table{
                    border-collapse: collapse;
                }
                td, th {
                    border: 10px solid #cccccc;
                    padding-left: 20px;
                    padding-right: 10px;
                    padding-top: 5px;
                    padding-bottom: 5px;
                }
                th{
                    background-color: #cce6ff;
                }
                .first-th-style{
                    padding: 20px;
                    font-size: 20px;
                    color: #ffffff;
                    background-color: #004080
                }
            
            
            </style>

            '''
    cursor.execute(query, movie_code)
    row = cursor.fetchone()

    tr_list = ''
    td_text = ''

    count = 1
    while row:
        td_text += '<td>{0}</td>'.format(count)
        td_text += '<td>{0}{1}</td>'.format(row[1], row[2], row[4])
        tr_text = '<tr>{0}</tr>'.format(td_text)
        tr_list += tr_text
        count += 1
        row = cursor.fetchone()
        td_text = ''

    thead_text = '<thead><tr><th colspan="3" class="first-th-style">{0}</th></tr><tr><th>{1}</th><th>{2}</th></tr></thead>'.format("출연진 이름", "국적","배역 이름")
    tbody_text = '<tbody>{0}</tbody>'.format(tr_list)
    table_text = '<table>{0}{1}</table>'.format(thead_text,tbody_text)
    meta_text = '<meta http-equiv="Content-Type" content="text/html;" charset="utf-8" />'

    head_text = '<head><title>{0}</title>{1}{2}</head>'.format("영화 상세 정보", meta_text, style_text)
    body_text = '<body>{0}</body>'.format(table_text)
    

    html_text = '<html>{0}{1}</html>'.format(head_text, body_text)

    f = open('C:/python/07.27-12.1_CLOUD/python/8일차/navermovie02/{0}.html'.format(movie_code), 'w', encoding='utf8')
    f.write(html_text)
    f.close()