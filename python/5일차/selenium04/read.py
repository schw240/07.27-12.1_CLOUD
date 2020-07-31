import time
from model_finance import Finance

def CreateHtml(code):
    
    f = open('C:/07.27-12.1_CLOUD/python/finance/{0}.csv'.format(code))
    fin_list = list()

    for line in f.readlines()[1:]:
        items = line.split(',')

        _date, _open, _high, _low, _close, _adj_close, _volume = items;
        fin = Finance(code, _date, _open, _high, _low, _close, _adj_close, _volume)
        fin_list.append(fin)

    f.close()

    css_text = '''

        table {
            border: 1px solid #cccccc;
            border-collapse: collapse;
        }
        td, th{
            border: 1px solid #cccccc;
            padding: 6px;
        }
        th{
            background-color: #cce6ff;
        }
        .number-td-style{
            text-align: right;
            font-weight: bold;
            width: 200px;
            background-color: greenyellow;
        }
        .first-th-style{
            padding: 20px;
            font-size: 20px;
            color: #ffffff;
            background-color: #004080;
        }
    '''
    style_text = '<style>{0}</style>'.format(css_text)

    meta_text = '<meta http-equiv="Content-Type" content="text/html;" charset="utf-8" />'
    head_text = '<head>{1}{0}</head>'.format(meta_text,style_text)

    th_text = '<th>코드</th>'
    th_text += '<th>날짜</th>'
    th_text += '<th>시가</th>'
    th_text += '<th>상한가</th>'
    th_text += '<th>하한가</th>'
    th_text += '<th>종가</th>'
    th_text += '<th>adj_close</th>'
    th_text += '<th>거래량</th>'
    th_list_text = '<tr>{0}</tr>'.format(th_text)
    thead_text = '<thead>{0}</thead>'.format(th_list_text)

    tr_list_text = ''

    for fin in fin_list:
        td_text = '<td>{0}</td>'.format(fin.code)
        td_text += '<td>{0}</td>'.format(fin.date)
        td_text += '<td>{0}</td>'.format(fin.open)
        td_text += '<td>{0}</td>'.format(fin.high)
        td_text += '<td>{0}</td>'.format(fin.low)
        td_text += '<td>{0}</td>'.format(fin.close)
        td_text += '<td>{0}</td>'.format(fin.adj_close)
        td_text += '<td class="number-td-style">{0}</td>'.format(fin.volume)
        
        tr_text = '<tr>{0}</tr>'.format(td_text) # 전체 td_text에 tr 씌워주기 !!!!
        tr_list_text += tr_text

    #<tr><td></td></tr> 이 조합들은 <tbody>로 감싸주어야함
    tbody_text = '<tbody>{0}</tbody>'.format(tr_list_text)
    table_text = '<table>{0}{1}</table>'.format(tbody_text, thead_text)
    body_text = '<body>{0}</body>'.format(table_text)
    html_text = '<html>{0}{1}</html>'.format(head_text,body_text)

    f = open('C:/07.27-12.1_CLOUD/python/finance/{0}.html'.format(code), 'w', encoding='utf8')
    f.write(html_text)
    f.close()

