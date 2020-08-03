from adp_notebook import SearchNB
from adp_company import SearchCP
from adp_mall import SearchMall

command = ''

while command.upper() != 'EXIT':
    command = input('명령어를 입력하세요: ')
    if command == '1':
        nbs = SearchNB()
        for nb in nbs:
            nb.show()

    elif command == '2':
       cps = SearchCP()
       for cp in cps:
            cp.show()
            
    elif command == '3':
        malls = SearchMall()
        for mall in malls:
            mall.show()

    else:
        print('잘못입력하셨습니다.')
