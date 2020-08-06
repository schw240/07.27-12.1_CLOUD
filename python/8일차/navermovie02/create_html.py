import pymssql
from movie_detail import MovieDetail



ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def CreateHtml():
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT TITLE, GENRE, CODE FROM MOVIE_LIST ORDER BY CODE'
    cursor.execute(query)
    row = cursor.fetchone()

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
    movie_code_list = list()
    tr_list = ''
    td_text = ''
    count = 1

    while row:
        a_link = '<a href="C:/python/07.27-12.1_CLOUD/python/8일차/navermovie02/{0}.html">{1}</a>'.format(row[2], row[0])
        td_text += '<td>{0}</td>'.format(count)
        td_text += '<td>{0}</td>'.format(a_link)
        td_text += '<td>{0}</td>'.format(row[1])
        print(td_text)
        tr_text = '<tr>{0}</tr>'.format(td_text)
        print(tr_text)
        tr_list += tr_text
        print(tr_list)
        count += 1
        movie_code_list.append(row[2])
        row = cursor.fetchone()
        td_text = ''
        

    thead_text = '<thead><tr><th colspan="3" class="first-th-style">{0}</th></tr><tr><th>{1}</th><th>{2}</th><th>{3}</th></tr></thead>'.format("네이버 영화 평점 순위", "순위","영화", "장르")
    tbody_text = '<tbody>{0}</tbody>'.format(tr_list)
    table_text = '<table>{0}{1}</table>'.format(thead_text,tbody_text)
    meta_text = '<meta http-equiv="Content-Type" content="text/html;" charset="utf-8" />'

    head_text = '<head><title>{0}</title>{1}{2}</head>'.format("영화 목록", meta_text, style_text)
    body_text = '<body>{0}</body>'.format(table_text)
    

    html_text = '<html>{0}{1}</html>'.format(head_text, body_text)
    
    
    f = open('C:/python/07.27-12.1_CLOUD/python/8일차/navermovie02/MOVIE_LIST.html', 'w', encoding='utf8')
    f.write(html_text)
    f.close()
    
    #movie_code_list에 영화 코드 다 담겨있음
    for m_code in movie_code_list:
        MovieDetail(m_code)

    print("FINISH")
    