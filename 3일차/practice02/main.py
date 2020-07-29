from model_dog import Dog


dogs = list()
command = ''
##################################################################################################################
def Exist(name):
    isExist = False

    for dog in dogs:
        # 입력받은 name이 이미 존재하는 인스턴스의 이름과 같을 경우
        if dog.name == name:
            #중복된다고 알려줌
            isExist = True

    return isExist
##################################################################################################################
def InputInt(age):  
    num = None
    isNum = False

    # while 반복문을 통해 isNum이 False인 경우 계속 반복을 통해
    while isNum == False:
        
        try:    
            #나이를 입력받고
            text = input("나이를 입력해주세요:\t")
            #만약 입력받은 나이를 int형으로 변환 시켰을때 변환이 안될 경우에는 오류가 생김->프로그램 종료
            num = int(text)
            #만약 형변환이 된다면 숫자를 제대로 입력했다는 뜻으로 isNum이 True가 됌
            isNum = True
        except:
            #에러가 터져도 프로그램이 종료되지 않도록 해주며 try로 시도를 해보고 에러가 생기면 except로 넘어옴
            print('<<숫자를 입력해주세요!!!>>')
    return num
##################################################################################################################
def InputBool(msg):
    
    isneutral = None
    isboolean = False
    #isboolean이 False인 경우 계속 반복
    while isboolean == False:
        #입력받은 msg를 대분자로 변환하여 변수 text에 대입
        text = input(msg).upper()
        #만약 text가 'Y', 'N'인 경우에 맞게 isneutral을 True 또는 False로 변환
        #isneutral변수를 boolean으로 변환시켜주었기에 isboolean은 둘다 True로 변환해줌
        if text == "Y":
            isneutral = True
            isboolean = True
        elif text == "N":
            isneutral = False
            isboolean = True
        #만약 isboolean이 True로 변환이 안되고 똑같이 False인 경우 밑의 출력문을 출력하고
        #다시 반복문을 수행하게 됨
        if isboolean == False:
            print("잘못된 입력입니다. 영어로 Y 또는 N을 입력해주세요:\t")
    #만약 while문을 빠져나오면 isneutral을 반환(boolean 타입)
    return isneutral
##################################################################################################################
def AddDog():
    isExists = True
    while isExists == True:
        name = input("강아지 이름을 입력해주세요! :\t")
        isExists = Exist(name)
        if isExists == True:

            print("이미 등록되어있는 강아지입니다. 다시 입력해주세요.")

    age = InputInt("나이를 입력해주세요:\t")
    kind = input("견종을 입력해주세요:\t")
    isNeut = InputBool("중성화 유무를 입력해주세요: (Y/N)\t")
    d = Dog(name, kind, age, isNeut)
    dogs.append(d)
    print("강아지 <<{0}>>가 정상적으로 등록되었습니다.".format(d.name))
##################################################################################################################
def Search():
    print("<<조회 시작>>")
    for dog in dogs:
        dog.ShowProfile()
    print('<<조회 완료: 총 {0}마리 등록중>>'.format(len(dogs)))
##################################################################################################################
def Save():
    print("<<새로 추가한 강아지 저장>>")
    #w는 저장 open()을 통해 파일 오픈
    f = open('c:/python/3일차/practice02/dog_list.txt', 'w', encoding='utf8')
    for dog in dogs:
        line = dog.WriteLine()
        f.write(line)
    #항상 파일을 닫아주어야함 파일을 닫아야 저장이 됨
    f.close()
    print("파일이 저장되었습니다. (총: {0}건".format(len(dogs)))


    
##################################################################################################################
def Load():
    #기존에 남아있던 파일들을 날려주어야 로드할때마다 파일이 추가가 안됨 날려주기를 안할경우 append를 계속 하게 되어
    #이미 등록되어있던 목록들이 다시 append가 되어 중복되게 됨
    dogs.clear()

    print("<<기존 강아지 목록 불러오기>>")
    f = open('c:/python/3일차/practice02/dog_list.txt', 'r', encoding='utf8')
    for line in f.readlines(): #f.readlines()가 리스트이기때문에 한줄한줄을 읽어 line에 반복문을 통해 들어가게 됨
        #;를 통해 값을 쪼개서 items에 담음 #replace통해 개행문자 제거
        items = line.replace('\n', '').split(';')
        name = items[0]
        age = int(items[2])
        kind = items[1]
        neut = bool(items[3])

        dog = Dog(name, kind, age, neut)
        dogs.append(dog)
    f.close()
    print("파일이 로드되었습니다. (총: {0}건".format(len(dogs)))


##################################################################################################################
while command.upper() != "EXIT":

    command = input('기능\t<1: 추가  2: 조회  3: 저장  4: 로드  exit:종료>\n명령어 입력:\t')

    if command == "1":
        AddDog()
    elif command == "2":
        Search()
    elif command == "3":
        Save()
    elif command == "4":
        Load()


print("프로그램이 종료되었습니다.!")