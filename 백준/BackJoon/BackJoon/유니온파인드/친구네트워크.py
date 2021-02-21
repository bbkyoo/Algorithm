# 1. test_cases를 생성하고, for문을 돌린다.
# 2. parent, number를 딕셔너리형으로 받아주고
# 3. f에 친구 관계 수를 받는다.
# 4. x,y는 각 줄마다 두 명의 친구를 의미하고
# 5. 만약 x와 y가 부모노드에 없다면 추가해주고 number를 1로 설정한다.
# 6. 이후 union(x,y)를 통해 x←y연결 관계를 해주고
# 7. 우리는 x의 최종 Root 노드의 개수를 출력하면 끝이다.

import sys

input = sys.stdin.readline

def get_parent(x):
    if parent[x] == x:
        return x
    p = get_parent(parent[x]) 
    parent[x] = p
    return p

def union(x, y):
    x = get_parent(x)
    y = get_parent(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent(parent[x])

T = int(input())

for _ in range(T):
    parent = dict()
    number = dict()
    
    f = int(input())

    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
                
        union(x,y)
        print(number[get_parent(x)])
        # print(parent) 이해 안되면 
        # print(number) 이 주석 두개 풀어보기











