def CreateStockHtml(company_list):
    tr_list_text = ''
    for comp in company_list:
        a_link = '<a href="{0}.html">{0}</a>'.format(comp.symbol)
        td_text = '<td>{0}</td>'.format(comp.name)
        td_text += '<td>{0}</td>'.format(a_link)
        td_text += '<td>{0}</td>'.format(comp.market_cap)
        td_text += '<td>{0}</td>'.format(comp.ipo_year)
        tr_text = '<tr>{0}</tr>'.format(td_text)
        tr_list_text += tr_text

    table_text = '<table>{0}</table>'.format(tr_list_text)

    f = open('C:/07.27-12.1_CLOUD/python/finance/stocklist.html', 'w', encoding='utf8')
    f.write(table_text)
    f.close()