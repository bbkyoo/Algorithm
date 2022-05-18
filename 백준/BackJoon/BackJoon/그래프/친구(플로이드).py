n = int(input())

friends = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if friends[i][j] == 'Y' or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                    visited[i][j] = 1

result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1
    result = max(result, cnt)

print(result)
