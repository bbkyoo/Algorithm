# 방법1 dp로 풀었을때

#import sys

#input = sys.stdin.readline

#n = int(input())

#card = []
#for _ in range(n):
#    card.append(int(input()))

#table = [[0]*n for i in range(n)]
#for i in range(n - 1):
#    table[i][i+1] = card[i] + card[i+1]
#    for j in range(i+2, n):
#        table[i][j] = table[i][j-1] + card[j] 

#for d in range(2, n):
#    for i in range(n-d):
#        j = i+d
#        minimum = [table[i][k] + table[k+1][j] for k in range(i,j)]
#        table[i][j] += min(minimum)

#if n == 1:
#    print(0)
#else:
#    print(table[0][n-1])

# 방법2 우선순위 큐 또는 힙으로 풀때

import heapq 

n = int(input())
card = []

for _ in range(n):
    heapq.heappush(card, (int(input())))

answer = 0
while len(card) > 1: # 1개일 경우는 비교하지 않아도 된다.
    temp1 = heapq.heappop(card) # 제일 작은 수
    temp2 = heapq.heappop(card) # 두번쨰로 작은 수
    answer += (temp1 + temp2) # 현재 비교 횟수를 더해 줌
    heapq.heappush(card, temp1+temp2)

print(answer)

