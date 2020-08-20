from model_movie import Movie

movie_list = list()


command = ''
cnt = 0
while command.upper() != "EXIT":
    command = input('명령을 입력해주세요:\t')
    if command == '1':
        m = Movie(input('영화 제목을 입력해주세요!:\t'))
        cnt += 1 
        movie_list.append(m)
        m.show(cnt)