import random

# 삽입정렬
# 1. 삽입 정렬은 두 번째 인덱스부터 시작
# 2. 해당 인덱스(key) 앞에 있는 데이터부터 비교해서 인덱스값이 더 작으면, 데이터값을 뒤 인덱스로 복사
# 3. 이를 key값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동 

# 데이터 길이 2, 조건 1, 턴 1
# 데이터 길이 3, 최대 조건 2, 턴 2
# 데이터 길이 4, 최대 조건 3, 턴 3

def insertion_sort(data):
    for i in range(len(data)-1):
        for j in range(i+1, 0,-1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    return data

data = random.sample(range(100), 50)
data = insertion_sort(data)
print(data)

# 시간 복잡도
# O(n^2)
# 완전정렬 상태라면 O(n)




