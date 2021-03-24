import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
card = []

for _ in range(n):
    n1, n2, n3, n4, n5 = map(int, input().split())
    card.append([n1, n2, n3, n4, n5])

result = []
for i in card:
    temp = list(combinations(i, 3))
    sm = 0
    for j in temp:
        s = str(sum(j))
        sm = max(sm, int(s[-1]))

    result.append(sm)

answer = 0
for i in range(len(result)-1,-1,-1):
    if max(result) == result[i]:
        answer = i
        break

print(answer+1)