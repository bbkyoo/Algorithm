import sys

input = sys.stdin.readline

v, e = map(int, input().split())

matrix = []
for _ in range(e):
    a, b, c = map(int, input().split())
    matrix.append((c, a, b))

matrix.sort(key=lambda x : x[0])
parent = list(range(v+1))

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a]) # 경로 압축
    return parent[a]

sum = 0
for c, a, b in matrix:
    if find(a) != find(b):
        union(a, b)
        sum += c

print(sum)