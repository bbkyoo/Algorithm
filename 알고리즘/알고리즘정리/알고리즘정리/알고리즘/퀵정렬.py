import random

# 1. 퀵 정렬 이란
# 기준점(pivot)을 정해서, 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수를 작성함
# 각 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
# 함수는 왼쪽 + 기준점 + 오른쪽을 리턴함

# 2. 코드화
def qsort(data):
    if len(data) <= 1:
        return data

    left, right = [], []
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])

    return qsort(left) + [pivot] + qsort(right) 

# 3. 시간복잡도
# O(nlog(n)) 병합정렬과 유사
# 단 최악의 경우 (맨 처음 pivot이 가장 크거나, 가장 작으면)
# 모든 데이터를 비교하는 상황이 나옴
# O(n^2)
















