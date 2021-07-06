import random

# 선택정렬
# 1. 주어진 데이터 중, 최소값을 찾음
# 2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
# 3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

def selection_sort(data):
    for i in range(len(data)-1):
        mn = i
        for j in range(i+1, len(data)):
            if data[mn] > data[j]:
                mn = j
        data[i], data[mn] = data[mn], data[i]
    return data

data = random.sample(range(100), 50)
data = selection_sort(data)
print(data)

# 시간 복잡도
# O(n^2)