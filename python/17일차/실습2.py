# x=[3,6,9,20,-7,5]의값의모든요소에10을곱하여저장한뒤출력하세요
# 실행 :
# [30, 60, 90, 200, -70, 50]

x = [3,6,9,20,-7,5]

for i, item in enumerate(x):
    item = item * 10
    x[i] = item

print(x)