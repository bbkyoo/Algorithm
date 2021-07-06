import random

# 버블 정렬
# 인접한 두 데이터를 비교하여 , 앞에 있는 데이터가 뒤에 있는 데이터보다 크면 자리를 바꾼다. 

# 데이터 길이 2, 조건 체크 1, 한 바퀴 도는 것 1
# 데이터 길이 3, 조건 체크 2, 한 바퀴 도는 것 2
# 데이터 길이 4, 조건 체크 3, 한 바퀴 도는 것 3

# for i in range(데이터 길이 - 1):
#   for j in range(데이터 길이- i - 1):
#       if 앞 데이터 > 뒤 데이터:
#           swap(앞 데이터, 뒤 데이터)

def bubblesort(data):
    for i in range(len(data)-1):
        swap = False
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] 
                swap = True

        if swap == False:
            break

    return data

data = random.sample(range(100), 50)
data = bubblesort(data)
print(data)

# 시간 복잡도
# O(n^2)
# 완전 정렬 상태라면 O(n)




