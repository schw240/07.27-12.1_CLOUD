# (1) 이름, 나이, 연락처를 입력받아 딕셔터리를 만들어 출력해주세요
# 실행 :
# 이름을 입력해주세요 : 홍길동
# 나이를 입력해주세요 : 27
# 연락처를 입력해주세요 : 010-3023-1223
# {'이름': '홍길동', '나이': '27', '연락처': '010-3023-1223'}


#실습 1
dict_list = list()

command = ''
while command.upper() != "EXIT":
    command = input("명령어를 입력하세요: 1번 딕셔너리 요소 추가 / exit 종료: \t")
    if command == "1":
        print("딕셔너리 추가")
        my_dict = dict()
        while True:
            key = input("이름 , 나이 , 연락처 순:")
            val = input('입력')
            my_dict[key] = val
            con = int(input('1번은 계속 추가 , 2번은 종료'))
            if con == 2:
                break
        dict_list.append(my_dict)
    else:
        print("잘못된 명령어 입니다.")

print("딕셔너리 리스트:" , dict_list)