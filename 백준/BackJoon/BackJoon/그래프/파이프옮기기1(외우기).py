# 가로로 올 수 있는 경우의 수 -> (가로에서 가로로 가능, 대각선에서 가로로 가능) 이 경우의 수들의 합
# 세로로 올 수 있는 경우의 수 -> (세로에서 세로로 가능, 대각선에서 세로로 가능) 이 경우의 수들의 합
# 대각선으로 올 수 있는 경우의 수 -> (가로에서 대각선 가능, 세로에서 대각선 가능, 대각선에서 대각선 가능) 이 경우의 수들의 합
# 이 문제는 DFS로 풀어야 시간초과가 안난다
# 0 -> 가로, 1 -> 세로, 2 -> 대각선 

from collections import deque
import sys

def bfs(x, y, shape):
    global count

    q = deque([])
    q.append([x, y, shape])

    while q:
        x, y, shape = q.popleft()

        if x == n-1 and y == n-1:
            count += 1

        if shape == 0 or shape == 2:
            if y + 1 < n:
                if matrix[x][y+1] == 0:
                    q.append([x, y+1, 0])
                    
        if shape == 1 or shape == 2:
            if x + 1 < n:
                if matrix[x+1][y] == 0:
                    q.append([x+1, y, 1])

        if shape == 0 or shape == 1 or shape == 2:
            if x + 1 < n and y + 1 < n:
                if matrix[x+1][y] == 0 and matrix[x][y+1] == 0 and matrix[x+1][y+1] == 0:
                    q.append([x+1, y+1, 2])

input = sys.stdin.readline

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
count = 0
bfs(0,1,0)
print(count)

# DFS 코드
#import sys
#input = sys.stdin.readline
#def dfs(x, y, direction):
#    global count
#    if x == n - 1 and y == n - 1: count += 1
#    if direction == 0:
#        if y + 1 < n and s[x][y + 1] == 0: dfs(x, y + 1, 0)
#        if x + 1 < n and y + 1 < n:
#            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
#                dfs(x + 1, y + 1, 2)
#    elif direction == 1:
#        if x + 1 < n and s[x + 1][y] == 0: dfs(x + 1, y, 1)
#        if x + 1 < n and y + 1 < n:
#            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
#                dfs(x + 1, y + 1, 2)
#    elif direction == 2:
#        if y + 1 < n and s[x][y + 1] == 0: dfs(x, y + 1, 0)
#        if x + 1 < n and s[x + 1][y] == 0: dfs(x + 1, y, 1)
#        if x + 1 < n and y + 1 < n:
#            if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
#                dfs(x + 1, y + 1, 2)
#n = int(input())
#s = [list(map(int, input().split())) for i in range(n)]
#count = 0
#dfs(0, 1, 0)
#print(count)