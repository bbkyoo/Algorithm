# https://it-garden.tistory.com/345

from collections import deque
import sys

input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    ch[n][0] = 0
    ch[n][1] = 1

    while q:
        x = q.popleft()

        for i in (x+1, x-1, x*2):
            if 0 <= i < 100001:
                if ch[i][0] == -1:
                    ch[i][0] = ch[x][0] + 1
                    ch[i][1] = ch[x][1]
                    q.append(i)

                elif ch[i][0] == ch[x][0] + 1:
                    ch[i][1] += ch[x][1]

n, k = map(int, input().split())

ch = [[-1,0] for _ in range(100001)]

bfs(n)
print(ch[k][0])
print(ch[k][1])
