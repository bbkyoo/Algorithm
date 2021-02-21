import sys

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
mn = float('inf')

def solve(k, j): # 여기 j가 시간을 줄이는데 가장가장가장가장 중요 이거 꼭 넣어서 시간 줄여야함
    global mn

    if k == n//2:
        link = []
        start = []
        
        for i in range(n):
            if visited[i] == 1:
                start.append(i)
            else:
                link.append(i)
        
        st = 0
        li = 0
        for i in range(n//2):
            for j in range(i+1, n//2):
                st += (s[start[i]][start[j]] + s[start[j]][start[i]]) 
                li += (s[link[i]][link[j]] + s[link[j]][link[i]])
        
        if st > li and mn > (st - li):
            mn = st - li
        elif st <= li and mn > (li - st):
            mn = li - st

        return

    else:
        for i in range(j, n): 
            if not visited[i]:
                visited[i] = 1
                solve(k+1, i)
                visited[i] = 0

visited[0] = 1
solve(1, 0)
print(mn)
