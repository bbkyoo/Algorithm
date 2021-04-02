import re
import sys

input = sys.stdin.readline

n = int(input())

s = []
for _ in range(n):
    s.append(input().rstrip())

q = int(input())

sch = []
for _ in range(q):
    sch.append(input().rstrip())

result = []
for i in sch:
    count = 0
    for j in s:
        if re.search(i, j):
            count += 1
    result.append(count)

for i in result:
    print(i)