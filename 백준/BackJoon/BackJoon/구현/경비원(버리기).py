# 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다.
# 둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고
# 상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리를 나타낸다

import sys

input = sys.stdin.readline

m, n = map(int, input().split())
store_count = int(input())
matrix = [[0]*m for _ in range(n)]

for _ in range(store_count):
    x, y = map(int, input().split()) 
    if x == 1:
        matrix[0][y-1] = 1
    elif x == 2:
        matrix[n-1][y-1] = 1
    elif x == 3:
        matrix[y-1][0] = 1
    else:
        matrix[y-1][n-1] = 1

target_x, target_y = map(int, input().split())
if target_x == 1:
    target_x = 0
    target_y = target_y - 1 
elif target_x == 2:
    target_x = n-1
    target_y = target_y - 1
elif target_x == 3:
    target_x = target_y - 1 
    target_y = 0
else:
    target_x = target_y - 1 
    target_y = n-1
 
sum = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            if target_x == n-1:
                if i == n-1:
                    mn = abs(target_y - j)
                elif i == 0: 
                    mn = min(j+1+target_y+1+n, m-(target_y+1) + m-(j+1) + n )
                elif j == 0:
                    mn = abs(n-(i+1)) + target_y + 1
                elif j == m-1:
                    mn = abs(n-(i+1)) + abs(m - (target_y + 1))
            elif target_x == 0:
                if i == 0:
                    mn = abs(target_y - j) 
                elif i == n-1: 
                    mn = min((j+1+target_y+1+n),m-(j+1) + m-(target_y+1)+n)
                elif j == m-1:
                    mn = i+1 + m - (target_y + 1)
                elif j == 0:
                    mn = i+1 + target_y + 1
            elif target_y == 0:
                if i == 0:
                    mn = target_x + 1 + j + 1
                elif i == n-1: 
                    mn = n - (target_x + 1) + j + 1
                elif j == m-1:
                    mn = min(target_x+1 +i+1+m, m+n-(target_x+1)+n-(i+1))
                elif j == 0:
                    mn = abs(i - target_x) 
            elif target_y == m-1:
                if i == 0:
                    mn = target_x + 1 + m - (j + 1)
                elif i == n-1: 
                    mn = n - (target_x + 1) + m-(j + 1)
                elif j == m-1:
                    mn = abs(i - target_x) 
                elif j == 0:
                    mn = min(m+n-(i+1)+ n-(target_x+1), i+1+target_x+1+m)
            sum += mn

print(sum)

            




























