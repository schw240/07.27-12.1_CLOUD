from model_player import Player


p1 = Player("플레이어1", "O")
p2 = Player("플레이어2", "X")
turn = 0

def create_board():
    a,b = input().split()
    a = int(a)
    b = int(b)
    board = [['+']* a]*b
    return board, a, b


def chk_win_row(omok_board, a, b):
    for i in range(a):
        cnt = 0
        cnt2 = 0
        for j in range(b):
            if omok_board[a][b] == '+':
                continue
            elif omok_board[a][b] == 'O':
                cnt+=1
                if cnt== 5:
                    print("player1이 승리하셨습니다.")
                    exit()
            elif omok_board[a][b] == 'X':
                cnt2+=1
                if cnt2 == 5:
                    print("player2이 승리하셨습니다.")
                    exit()


# def chk_win_col(omok_board, a, b):
#     cnt = 0
#     for i in range(a):
#         for j in range(b):
#             if omok_board[b][a] == 'O':
#                 cnt+=1
#                 if cnt+= 5:
#                     print("player1이 승리하셨습니다.")
#                     exit()
#         cnt = 0
#             if omok_board[b][a] == 'X':
#                 cnt+=1
#                 if cnt+= 5:
#                     print("player2이 승리하셨습니다.")
#                     exit()
#         cnt = 0
                     
            

def do_p1(omok_board, a, b):
    omok_board[a][b] = 'O'
    return omok_board


def do_p2(omok_board, a, b):
    omok_board[a][b] = 'X'
    return omok_board

omok_board, a, b = create_board()

while True:
    turn += 1
    if turn%2 == 1:
        #p1차례
        a, b = input().split()
        a = int(a)
        b = int(b)
        do_p1(omok_board, a, b)
        chk_win_row(omok_board, a, b)
        turn += 1
    elif turn%2 == 0:
        c, d = input().split()
        c = int(c)
        d = int(d)
        #p2차례
        do_p2(omok_board, c, d)
        chk_win_row(omok_board, a, b)
        turn += 1

