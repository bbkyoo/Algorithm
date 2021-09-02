import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split()) 
    building = [0] + list(map(int, input().split())) # 각 건물들의 건설시간
    tree = [[] for _ in range(n+1)] # 건설순서규칙
    inDegree = [0 for _ in range(n+1)] # 진입차수
    dp = [0 for _ in range(n+1)] # 해당 건물까지 걸리는 시간

    for _ in range(k): # 건설 규칙 저장
        x, y = map(int, input().split())
        tree[x].append(y)
        inDegree[y] += 1

    q = deque()
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = building[i]

    while q:
        a = q.popleft()
        for i in tree[a]:
            inDegree[i] -= 1 # 진입차수 줄이고 비용갱신
            dp[i] = max(dp[a] + building[i], dp[i]) # dp를 이용해 건설비용 갱신
            if inDegree[i] == 0:
                q.append(i)

    answer = int(input())
    print(dp[answer])