# https://suri78.tistory.com/11

import sys

input = sys.stdin.readline

alpha1 = list(input().strip())
alpha2 = list(input().strip())

len1 = len(alpha1)
len2 = len(alpha2)

matrix = [[0]*(len2 +1) for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if alpha1[i-1] == alpha2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1 
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])