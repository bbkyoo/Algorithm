import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    x, y = map(int, input().split())
    matrix.append([x, y])

costs = []
parent = list(range(n))

m_count = 0
for _ in range(m):
    x, y = map(int, input().split())
    if find(x-1) != find(y-1):
        union(x-1, y-1)
        m_count += 1

for i in range(n-1):
    for j in range(i+1, n):
        a = matrix[i]
        b = matrix[j]
        dist = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
        costs.append([dist, i, j])

costs.sort()        
answer = 0
for dist, i, j in costs:
    if find(i) != find(j):
        union(i, j)
        answer += dist
        m_count += 1
    if m_count == n-1:
        break

print("%0.2f"%answer)