# 이게 왜 안되는지 질문

#from collections import deque

#import sys

#input = sys.stdin.readline

#dx = [-1,1,0,0]
#dy = [0,0,-1,1]

#def bfs(x,y):
#    global answer

#    q = deque()
#    q.append([x,y,matrix[x][y]])

#    while q:
#        x, y, ans = q.popleft()
#        for i in range(4):
#            nx = x + dx[i]
#            ny = y + dy[i]
#            if 0 <= nx < R and 0 <= ny < C:
#                if matrix[nx][ny] not in ans:
#                    q.append([nx,ny,ans + matrix[nx][ny]]) 
#                    answer = max(answer, len(ans) + 1)

#R, C = map(int, input().split())

#matrix = [list(map(str, input())) for _ in range(R)]
#answer = 1
#temp = []

#bfs(0,0)

#print(answer)

# 집합을 쓰면 머가 달라지는거지?

import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global answer

    q = set([(x,y,matrix[x][y])]) # 집합 자료형은 다음과 같이 set 키워드를 사용해 만들 수 있다. 

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if matrix[nx][ny] not in ans:
                    q.add((nx,ny,ans + matrix[nx][ny])) # 집합 자료형에서 원소를 추가할 때
                    print(q)
                    answer = max(answer, len(ans) + 1)

R, C = map(int, input().split())

matrix = [list(map(str, input().strip())) for _ in range(R)]
answer = 1
temp = []

bfs(0,0)

print(answer)



