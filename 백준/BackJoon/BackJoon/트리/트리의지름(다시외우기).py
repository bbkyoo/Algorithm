# 노드 x에서 가장 먼 노드를 y라고 했을때 y는 지름을 이루는 노드중 하나이다.
# 이 문제는 임의의 노드 x에 대해 DFS(x)에서의 최장거리를 이루는 y를 구하고 DFS(y)를 구해 최장길이를 구하는 문제이다.

import sys

input = sys.stdin.readline
v = int(input())

matrix = [[] for _ in range(v+1)]

for _ in range(v):
    path = list(map(int, input().split()))   

    path_len = len(path)
    for i in range(1, path_len//2):
        matrix[path[0]].append([path[2*i - 1], path[2*i]]) # 이 대입 코드를 잘 기억해 둘 것

# 첫 번째 DFS결과

result1 = [0 for _ in range(v+1)]

def DFS(start, matrix, result):
    for e,d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            DFS(e,matrix,result)

DFS(1, matrix, result1) # 아무노드에서 시작해준다.
result1[1] = 0 # 루트 노드가 정해져 있지않아 양방향으로 입력을 받기때문에 해당

tmpmax = 0 # 최댓값 구하기
index = 0 # 최장경로 노드

for i in range(len(result1)):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

# 최장경로 노드에서 다시 DFS를 통해 트리지름구하기
result2 = [0 for _ in range(v+1)]
DFS(index, matrix, result2)
result2[index] = 0
print(max(result2))




