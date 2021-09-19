import sys

inf = sys.maxsize

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
s = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    s[a-1][b-1] = min(s[a-1][b-1], l)
    s[b-1][a-1] = min(s[b-1][a-1], l)

for k in range(n):
    for i in range(n):
        for j in range(n):
            s[i][j] = min(s[i][j], s[i][k] + s[k][j])
            if i == j:
                s[i][j] = 0

max_value = 0

for i in range(n):
    temp_value = 0
    for j in range(n):
        if s[i][j] <= m:
            temp_value += t[j]

    max_value = max(max_value, temp_value)

print(max_value)