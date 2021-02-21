import sys

input = sys.stdin.readline

def get_parent(x):
    if parent[x] == x:
        return x
    p = get_parent(parent[x])
    parent[x] = p
    return p

def union(x,y):
    x = get_parent(x)
    y = get_parent(y)

    if x != y:
        parent[y] = x

def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent(parent[x])

n = int(input())
m = int(input())

parent = {}

for i in range(n+1):
    parent[i] = i

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))

istrue = True
for i in range(1, len(plan)):
    if find_parent(plan[i-1]) != find_parent(plan[i]):
        istrue = False

if istrue == True:
    print("YES")
else:
    print("NO")













