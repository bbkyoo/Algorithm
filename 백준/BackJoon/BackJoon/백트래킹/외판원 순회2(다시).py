import sys

def dfs(start, next, value, visited):
    global min_value

    if len(visited) == n:
        if w[next][start] != 0:
            min_value = min(min_value, value + w[next][start])
        return

    for i in range(n):
        if w[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + w[next][i], visited)
            visited.pop()

n = int(input())

w = []
min_value = sys.maxsize
for _ in range(n):
    w.append(list(map(int, input().split())))

for i in range(n):
    dfs(i, i, 0, [i])

print(min_value)