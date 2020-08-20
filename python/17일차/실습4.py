# word=[“school”,“game”,“piano”,“science”,“hotel”,“mountian”]중글자수가6글자
# 이상인문자를모아새로운리스트를생성하세요
# 실행 :
# ['school', ' science', 'mountain']

word=['school','game','piano','science','hotel','mountain']


new_list = list()
for item in word:
    if len(item) >= 6:
        #print(len(item))
        new_list.append(item)

print(new_list)