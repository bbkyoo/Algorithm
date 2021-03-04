#1 6 2 5 3 4 (6 - 2 = 4)
#1 2 5 3 4 (5 - 3 = 2)
#1 2 3 4 (4 - 3 = 1)
#1 2 3 (3 - 2 = 1)
#1 2 (2 - 1 = 1)

import sys

input = sys.stdin.readline

n = int(input())
m = n
lank = list(map(int, input().split()))
result = 0

while len(lank) != 1:
    index = lank.index(max(lank))
    if index+1 < m and 0 <= index-1:
        result += min(abs(lank[index] - lank[index+1]),  abs(lank[index] - lank[index-1]))
    elif index+1 < m and 0 > index-1:
        result += abs(lank[index] - lank[index+1])
    elif index+1 >= m and 0 <= index-1:
        result += abs(lank[index] - lank[index-1])
    elif index+1 >= m and 0 > index-1:
        result += lank[index]

    lank.pop(index)
    m -= 1

print(result)