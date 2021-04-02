import sys

input = sys.stdin.readline

n, k = map(int, input().split())

cal = k
numC = 0
numL = 1
total = 0

while cal > numC * numL :
    total += numC
    cal -= numC * numL
    numC *= 10
    numL += 1

total += (cal-1)//(numL+1) 

tenten = 1
result = 0

if total > n:
    result = -1

else:
    temp = ((cal-1) % numL) + 1

    for i in range(numL-1):
        tenten *= 10

    for i in range(temp):
        result = total//tenten
        total %= tenten
        tenten //= 10

print(result)





