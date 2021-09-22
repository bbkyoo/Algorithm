import sys

input = sys.stdin.readline
inf = 100000000

V, E = map(int, input().split())

s = [[inf] * V for i in range(V)]

for _ in range(E):
    a,b,c = map(int, input().split())
    s[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

result = inf
for i in range(V):
    result = min(result, s[i][i])
if result == inf:
    print(-1)
else:
    print(result)
