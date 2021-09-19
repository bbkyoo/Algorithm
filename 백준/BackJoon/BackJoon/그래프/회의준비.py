import sys

inf = sys.maxsize

n = int(input())
m = int(input())

s = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                s[i][j] = 0
                continue

            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

print(s)

    #1 2 3 4 5 6 7 8 
    
    #1 -> 2
    #2 -> 3
    #4 -> 5
    #5 -> 6
    #4 -> 6
    #6 -> 7
    #7 -> 4