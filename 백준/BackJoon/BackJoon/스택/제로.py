import sys

k = int(sys.stdin.readline())

nums = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)    

print(sum(nums))