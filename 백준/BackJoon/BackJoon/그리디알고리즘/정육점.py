# https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2258%EB%B2%88-%EC%A0%95%EC%9C%A1%EC%A0%90%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-3%EB%93%B1

import sys

input = sys.stdin.readline

def getMinCost(arr):
# 무게에 대해서도 정렬해주는 것은, 같은 가격의 고기들을 살 때 고중량 고기를 먼저 사야겠다는 것이다.
    arr.sort(key=lambda x:(x[1],-x[0]))

    weightCount = 0
    sameCostCount = 0
    costList = []

    for i in range(n):
        w, c = arr[i]

        weightCount += w
        # 1. 같은 가격인 고기들을 여러 개 살 경우
        if i >= 1 and c == arr[i-1][1]:
            sameCostCount += c
        # 2. 일반적인 경우, 이전 고기보다 현재 고기가 비쌀 경우
        else:
            sameCostCount = c

        if weightCount >= m:
            costList.append(sameCostCount)

            # 2의 경우인데 목표 중량을 달성했을 경우에는 더이상 반복문을 돌릴 필요가 없다.
            if sameCostCount == c:
                break

    if costList:
        return min(costList)
    else:
        return -1

n, m = map(int, input().split())
arr = []
for _ in range(n):
    weight, money = map(int, input().split())
    arr.append([weight, money])

result = getMinCost(arr)
print(result)