import sys

input = sys.stdin.readline

n = int(input())
row = []

for _ in range(n):
    x, y = map(int, input().split())
    row.append([x,y])

currnt = row.pop(0)
sum = 0

while row:
    if currnt[0] <= row[0][0] <= currnt[1] and currnt[1] <= row[0][1]:
        currnt = [currnt[0], row[0][1]]
    elif currnt[0] <= row[0][0] <= currnt[1] and currnt[1] > row[0][1]:
        currnt = [currnt[0], currnt[1]]
    else:
        sum += abs(currnt[1] - currnt[0])
        currnt = [row[0][0], row[0][1]]

    row.pop(0)

sum += abs(currnt[1] - currnt[0])
print(sum)













