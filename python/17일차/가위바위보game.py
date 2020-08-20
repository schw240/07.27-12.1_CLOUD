import random

        
def usr_choice():
    rsp = ''
    rsp = int(input("가위(1), 바위(2), 보(3)를 숫자로 입력해주세요:"))
    if rsp == 1:
        return "유저: 가위"
    elif rsp == 2:
        return "유저: 바위"
    elif rsp == 3:
        return "유저: 보"       
    else:
        return -1
        

def com_choice():
    com = random.randint(1,3)
    if com == 1:
        return "컴퓨터: 가위"
    elif com == 2:
        return "컴퓨터: 바위"
    elif com == 3:
        return "컴퓨터: 보"      


cnt = 0
win = 0
while True:
    user = usr_choice()
    computer = com_choice()
    if user == "유저: 가위" and computer == "컴퓨터: 가위":
        print(user, computer)
        cnt += 1
    elif user == "유저: 가위" and computer == "컴퓨터: 바위":
        print(user, computer)
        cnt += 1
    elif user == "유저: 가위" and computer == "컴퓨터: 보":
        print(user, computer)
        cnt += 1
        win += 1

    elif user == "유저: 바위" and computer == "컴퓨터: 가위":
        print(user, computer)
        cnt += 1
        win +=1
    elif user == "유저: 바위" and computer == "컴퓨터: 바위":
        print(user, computer)
        cnt += 1
    elif user == "유저: 바위" and computer == "컴퓨터: 보":
        print(user, computer)
        cnt += 1
    
    elif user == "유저: 보" and computer == "컴퓨터: 가위":
        print(user, computer)
        cnt += 1
    elif user == "유저: 보" and computer == "컴퓨터: 바위":
        print(user, computer)
        cnt += 1
        win += 1
    elif user == "유저: 보" and computer == "컴퓨터: 보":
        print(user, computer)
        cnt += 1

    elif user == -1:
        break

print('전체:{0}, 승리:{1}'.format(cnt, win))