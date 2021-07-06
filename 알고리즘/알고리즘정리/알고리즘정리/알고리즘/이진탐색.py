import random

# 1. 이진 탐색 이란?
# 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법

# 2. 분할 정복 알고리즘과 이진 탐색

# 분할 정복 알고리즘
# 문제를 하나또는 둘 이상으로 나눈다, 나눠진 문제가 충분히 작고 해결이 가능하면 해결하고 아니면 다시 나눈다

# 이진 탐색
# 검색할 숫자 > 중간값 이면, 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다
# 검색할 숫자 < 중간값 이면, 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다 

# 3. 구현
def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True

    if len(data) == 1 and search != data[0]:
        return False

    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)

data = random.sample(range(100), 100)
data.sort()
print(binary_search(data, 7))

# 시간 복잡도
# O(log(n))



