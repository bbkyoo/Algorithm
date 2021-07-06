import math
import sys

sys.setrecursionlimit(10**5)

def dps(matrix, visited, loc):
    visited[loc] = 1

    for i in range(len(matrix)):
        if visited[i] == 0:
            ln = math.sqrt(math.pow(matrix[loc][0]-matrix[i][0], 2) + math.pow(matrix[loc][1]-matrix[i][1], 2))
            if ln <= matrix[loc][2] + matrix[i][2]:
                dps(matrix, visited, i)

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    visited = [0]*n

    for _ in range(n):
        x, y, r = map(int, input().split())
        matrix.append([x,y,r])

    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            dps(matrix, visited, i)
            cnt += 1

    print(cnt)

