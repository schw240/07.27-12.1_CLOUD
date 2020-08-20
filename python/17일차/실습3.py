# y={“math”:70,“science”:80,“english”:20}의값의모든요소에10을더하여저장한뒤출력하세요
# 실행 :
# {'math': 80, 'science': 90, 'english': 30}

y = dict()
y = {'math':70, 'science':80, 'english':20}

for key, val in y.items():
    val += 10
    y[key] = val

print(y)