import random


#인덱스 기법
def get_median1(data):
    sorted(data)
    center_idx = len(data) // 2 # 중앙인덱스 구하기

    return (data[center_idx] + data[-center_idx-1])/2

def get_median2(data):
    sorted(data)
    center_idx = len(data) // 2 # 중앙인덱스 구하기

    if (len(data) % 2) == 1:
        return data[center_idx]
    else:
        return (data[center_idx-2] + data[center_idx-1] / 2)

data = [1,2,3,4,5,6]

print(get_median2(data))
