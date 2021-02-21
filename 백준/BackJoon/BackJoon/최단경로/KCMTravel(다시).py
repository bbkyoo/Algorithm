import heapq
import sys

input = sys.stdin.readline

T = int(input())
inf = sys.maxsize

for _ in range(T):
    n, m, k = map(int, input().split())
    ticket = [[] for i in range(n+1)]

    for _ in range(k):
        u, v, c, d = map(int, input().split())   
        ticket[u].append([v,c,d])
      
    dp = [[inf for _ in range(m+1)] for _ in range(n+1)] # 열 : 비용 , 행 : n까지 갈때    
    dp[1][0] = 0 # 1 -> 1로 갔을때 비용은0 시간도0   

    for c in range(m+1):
        for d in range(1,n+1):
            if dp[d][c] == inf: # c의 비용으로 d에 도착하는 경우가 없다면
                continue
            t = dp[d][c] # c의 비용으로 d에 도착했을때 소요시간

            for nv,nc,nd in ticket[d]: #d에서 출발하는 모든 경우
                if nc + c > m: #비용이 초과될 경우 넘어간다
                    continue
                dp[nv][nc+c] = min(dp[nv][nc+c], t+nd) #이전에 저장된값과 비교하여 작다면 넣어준다

    result = min(dp[n]) # N에 도착할때 최소 소요시간

    if result == inf:
        print('Poor KCM')
    else:
        print(result)






