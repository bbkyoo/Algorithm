# https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

import sys

input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1


for i in range(n):
    for j in range(n):
        if j == n-1:
            print(matrix[i][j])
        else:
            print(matrix[i][j], end=' ')