import pickle

dict_list = list()
command = ''

while True:
    command = input('메뉴를 선택해주세요: 1 - 입력, 2 - 조회, 3 - 삭제, 4- 저장, 5- 로드 0 - 종료:')
    if command == '1':
        print('입력해주세요:')
        my_dict = dict()
        values = list()
        keys = ['이름' , '수학', '과학', '영어']
        
        for item in keys:
            val = input("이름 , 수학 , 과학 , 영어 순으로 값을 입력하세요: ")
            values.append(val)
        
        my_dict = {key: value for key, value in zip(keys,values) }        
        dict_list.append(my_dict)


    elif command == '2':
        cnt = 0
        print('조회를 시작합니다.')
        for item in dict_list:
            print("[{0}]{1}".format(cnt, item))
            cnt += 1
            
    elif command == '3':
        num = int(input("삭제할 번호를 입력해주세요: "))
        del dict_list[num]
        print("삭제가 완료되었습니다.")


    elif command == '4':
        print("저장")
        with open('C:/07.27-12.1_CLOUD/python/17일차/성적.p', 'wb') as file:
            pickle.dump(dict_list, file)

    elif command == '5':
        print('로드')
        with open('C:/07.27-12.1_CLOUD/python/17일차/성적.p', 'rb') as file:
            dict_list = pickle.load(file)

    elif command == '0':
         print("종료되었습니다.")
         break

