# 1. 집합 n+1개를 만들고 자기자신을 부모로 설정한다. (처음)
# 2. 부모를 합칠 때는 일반적으로 더 작은 값 쪽으로 합친다. 이것을 union(합침)
# 3. 만약 1, 2, 3 이 연결되어 있을때 1 과 3 은 부모가 각각 1과 2로 다르기 때문에 재귀를 사용하여 1 과 3이 연결되었는지 파악
  
import sys

input = sys.stdin.readline

# 부모노드를 찾는 함수 
def get_parent(x):
    if parent[x] == x:
        return x
    p = get_parent(parent[x])
    parent[x] = p
    return p

# 두 부모 노드를 합치는 함수
def union(x, y):
    x = get_parent(x)
    y = get_parent(y)

    if x != y: # 원래는 더 작은 값을 부모노드로 해야함
        parent[y] = x

# 같은 부모를 가지는지 확인
def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent(parent[x])

n, m = map(int, input().split())
parent = {}

for i in range(n+1): # 자기 자신을 부모로
    parent[i] = i

for _ in range(m):
    z, x, y = map(int, input().split())

    if not z:
        union(x, y)

    if z:
        if find_parent(x) == find_parent(y):
            print("YES")
        else:
            print("NO")
