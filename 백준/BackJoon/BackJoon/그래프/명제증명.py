# https://dallae7.tistory.com/63

from collections import deque
import sys

inf = int(1e9)

graph = [[inf]*(52) for _ in range(52)]

n = int(input())
for _ in range(n):
    a, b, c = input().split()

    a_ord = ord(a)
    c_ord = ord(c)

    # 소문자
    if a_ord >= ord('a'):
        a_ord = a_ord - (ord('a') - ord('Z') - 1)

    # 소문자
    if c_ord >= ord('a'):
        c_ord = c_ord - (ord('a') - ord('Z') - 1)

    a_ord = a_ord - ord('A')
    c_ord = c_ord - ord('A')

    graph[a_ord][c_ord] = 1

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(52):
    for b in range(52):
        if a == b:
            graph[a][b] = 0

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(52):
    for a in range(52):
        for b in range(52):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

arr = []

# 수행된 결과를 출력
for a in range(52):
    for b in range(52):
        # 도달할 수 없는 경우, 무한 이라고 출력
        if graph[a][b] == 0 or graph[a][b] == 1e9:
            pass
        # 도달할 수 있는 경우 거리를 출력
        else:
            arr.append(a)
            arr.append(b)

print(len(arr)//2)

for i in range(0, len(arr), 2):
    a = arr[i]
    c = arr[i+1]

    # 소문자
    if a > 25:
        a = a + (ord('a') - ord('Z') - 1)

    if c > 25:
        c = c + (ord('c') - ord('Z') - 1)

    a = a + ord('A')
    c = c + ord('A')

    print("%c => %c" % (chr(a), chr(c)))

















