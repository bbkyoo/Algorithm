import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

n = int(input())

matrix = []
for _ in range(n):
    x, y = map(float, input().split())
    matrix.append([x, y])

matrix.sort()
parent = list(range(n))
costs = {} # {(별1, 별2): distance} 형태의 딕셔너리

# 모든 별들 간에 간선이 있다고 가정 => 비용 계산하여 저장
for i in range(n):
    for j in range(i+1, n):
        a = matrix[i]
        b = matrix[j]
        dist = round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5, 2)
        costs[(i, j)] = dist

# 크루스칼 알고리즘을 위해 distance를 오름차순으로 정렬
costs = sorted(costs.items(), key=lambda x:x[1])

# 크루스칼 알고리즘
answer = 0
while costs:
    cur = costs.pop(0)
    a, b = cur[0]
    cost = cur[1]

    #같은 그룹에 있는 것이 아니라면
    if find(a) != find(b):
        answer += cost
        union(a, b)
    
print(answer)