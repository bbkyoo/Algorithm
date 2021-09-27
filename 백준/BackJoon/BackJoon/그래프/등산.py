import sys
from collections import defaultdict

input = sys.stdin.readline
inf = sys.maxsize

n, m, t, d = map(int, input().split())

dic = defaultdict()
for i in range(26):
    dic[chr(65+i)] = i

for i in range(97, 123):
    dic[chr(i)] = (i - 71)

matrix = []
for _ in range(n):
    row = list(input().strip())
    for i in range(len(row)):
        row[i] = dic[row[i]] 
    matrix.append(row)




