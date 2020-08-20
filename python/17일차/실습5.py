# [3,6,9,20,-7,5]리스트를sort와같은함수를사용하지말고for문을활용하여
# 오름차순으로정렬해주세요.
# 실행 :
# [-7, 3, 5, 6, 9, 20]

a = [3,6,9,20,-7,5]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
