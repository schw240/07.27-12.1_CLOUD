#print("Hello, Python!")

# name = '김한주'
# address = '용인시 기흥구 중동'
# post = 16988
# use_yn = True

# print(name, address, post, use_yn)

# 메서드

# def GetName():
#     #name = input('이름을 입력하세요: ')
#     print("김한주")

# GetName()
# GetName()
# GetName()
# GetName()
# GetName()
# GetName()
# GetName()

# def CreateMessage(name, email):
#     #print('좋은 아침입니다.')
#     msg = "{0} ({1})님! 환영합니다.".format(name, email)
#     return msg

# #WelcomeMessage("김한주")
# #WelcomeMessage("이인섭")
# #WelcomeMessage("고미숙")

# message = CreateMessage('김한주', 'schw240@naver.com')

# print(CreateMessage('김한주', 'schw240@gmail.com'))
# print(message)



#--------------------------------------------------------------------------------------
# 리스트

# nations = list()

# #print(type(nations))
# nations.append('한국')
# nations.append('미국')
# nations.append('영국')
# nations.append('중국')
# nations.append('태국')
# nations.append('일본')

# # print(nations)
# # print(nations[0])
# # print(nations[1])
# # print(nations[2])


# #-------------------------------------------------------------------------------------------
# #반복문

# for n in nations:
#     print(n)

#리스트 안에 또 다시 리스트를 넣는것 가능 -> 이를 통해 여러 정보 저장


# command = ''

# while command.upper() != "EXIT":
#     command = input('명령어를 입력해주세요: ')

#     print('입력한 명령어: {0}'.format(command))    

# print('종료되었습니다.')

#------------------------------------------------------------------------------------------------
# 종합프로그래밍

#과일 또는 채소를 계속 입력받아 list에 추가하는 프로그램 만들기

# fruits = list()
# vegs = list()
# command = ''

# def AddItem(items, message):
#     item = input(message)
#     items.append(item)

#     return items


# # shift + tab을 누르면 들여쓰기 맞춰짐
# def PrintItem(items):
#     for item in items:
#         print(item)


# while command.upper() != 'EXIT':
#     command = input("명령어를 입력해주세요: ")
    
#     if command == "과일":
#         AddItem(fruits, "과일을 입력해주세요: ")
#     elif command == "채소":
#         AddItem(vegs, "채소를 입력해주세요: ")
#     elif command == "과일출력":
#         PrintItem(fruits)
#     elif command == "채소출력":
#         PrintItem(vegs)
#     else:
#         print("명령어가 잘못되었습니다. 다시 입력해주세요!")


#--------------------------------------------------------------------------------------------------------
#클래스

from model_hero import HeroModel



# heroes = list()
# #히어로모델이라는 클래스를 새로 생성해줌
# #ironman, hulk, thor들은 인스턴스
# ironman = HeroModel("아이언맨", "미국", "마크50", "red")
# hulk = HeroModel("헐크", "미국", "그뉵", "green")
# thor = HeroModel("토르", "미국", "묠니르", "gold")
# #print(type(hero))

# heroes.append(HeroModel('Hulk', 'muscle', '미국', 50))
# heroes.append(HeroModel('Ironman', 'mark50', '미국', 55))
# heroes.append(HeroModel('Thor', 'myolnir', '미국', 500))
# heroes.append(HeroModel('Blackpensor', 'pensorsuit', '미국', 35))
# heroes.append(HeroModel('Blackwidow', 'gun', '미국', 38))
# heroes.append(HeroModel('Captin america', 'shield', '미국', 240))


# #ctrl + x 를 누르면 해당 줄 코드 잘라짐
# for hero in heroes:
#     name = hero.upper()
#     nation = hero.lower()
#     print(name, nation)
    
#     hero.ShowProfile()
    

# #파일을 불러와서 읽고 쓰기
# f = open('c:/python/heroes.txt', 'w', encoding='utf8')

# for h in heroes:
#     f.write(h.WriteLine())
#     #f.write('\n')
# f.close()

newheroes = list()

def ExistHero(name):
    isExists = False
    
    for hero in newheroes:
        if hero.name == name:
            isExists = True

    return isExists

def addHero():
    name = input('추가할 히어로명을 입력하세요: ')

    if ExistHero(name) == True:
        print('입력한 이름은 이미 등록된 정보입니다. >> {0}'.format(name))
    else:
        nation = input('추가할 히어로의 국가를 입력해주세요: ')
        age = int(input('추가할 히어로의 나이를 입력해주세요: '))
        armor = input('추가할 히어로의 무기를 입력해주세요: ')
        ishero = input('현재 히어로 활동 여부를 입력해주세요: ')

        newHero = HeroModel(nation, name, age, armor, ishero)
        newheroes.append(newHero)
        print('정상 등록되었습니다. >> {0}'.format(name))
        #name이 newheroes 리스트 안에 이미 존재하는지를 확인

def loadLine():
    print('히어로 목록을 불러옵니다.')
    f = open('c:/python/heroes.txt', 'r', encoding='utf8')
    for line in f.readlines():
        strHero = line.replace('\n', '') #replace를 통해 \n 제거
        heroLines = strHero.split(';')
        nation = heroLines[0]
        name = heroLines[1]
        age = int(heroLines[3])
        armor = heroLines[2]
        ishero = bool(heroLines[4])
        hero = HeroModel(nation, name, age, armor, ishero)
        newheroes.append(hero)
        f.close()
        print('데이터가 로드되었습니다. 총: {0}건'.format(len(newheroes)))

def saveLine():
    print("히어로 목록을 저장하겠습니다.")
    f = open('c:/python/heroes.txt', 'w', encoding='utf8')

    for h in newheroes:
        f.write(h.WriteLine())
    f.close()
    print('데이터가 저장되었습니다. 총: {0}건'.format(len(newheroes)))


def searchHero():
    for h in newheroes:
        h.ShowProfile()




command = ''
while True:
    command = input('명령어를 입력해주세요: \n (1: 추가 \t2: 조회\t3: 저장\t4: 로드\t종료를 원하면 exit를 입력하세요.)')

    if command == '1':
        addHero()
    elif command == '2':
        searchHero()
    elif command == '3':
        saveLine()
    elif command == '4':
        loadLine()
    elif command.upper() == 'EXIT':
        break
    else:
        print('없는 기능입니다.')

print('종료합니다.')