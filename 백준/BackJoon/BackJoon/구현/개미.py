import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l, n = map(int, input().split())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    
    nums.sort()        
    
    mx = max(l-nums[0], nums[-1])
    mn = min(abs(l - nums[0]), abs(nums[0] - 0))

    for i in range(1,n):
        temp = min(abs(l - nums[i]), nums[i])
        mn = max(mn, temp)

    print(mn, mx)


