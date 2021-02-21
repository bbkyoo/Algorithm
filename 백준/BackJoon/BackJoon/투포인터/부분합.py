import sys

input = sys.stdin.readline

n, s = map(int, input().split())
number = list(map(int, input().split()))
end = 0
sum = 0
length = n
isTrue = False

for start in range(n):   
    while end < n and sum < s: 
        sum += number[end]
        end += 1

    if sum >= s:
        isTrue = True
        if end - start < length:
            length = end - start
    sum -= number[start]

if isTrue:
    print(length)
else:
    print(0)

