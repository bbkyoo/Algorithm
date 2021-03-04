import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())
target = [e,s,m]
arr = [1,1,1]
result = 1

while arr != target:
    if 15 <= arr[0]:
        arr[0] = 1
    else:
        arr[0] += 1

    if 28 <= arr[1]:
        arr[1] = 1
    else:
        arr[1] += 1

    if 19 <= arr[2]:
        arr[2] = 1
    else:
        arr[2] += 1

    result += 1    

print(result)

