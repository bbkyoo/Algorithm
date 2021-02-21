from itertools import combinations

n, s = map(int, input().split()) 

nums = list(map(int, input().split()))
count = 0

for i in range(1,n+1):
    temp = list(combinations(nums, i))
    for j in range(len(temp)):
        if sum(temp[j]) == s:
            count += 1

print(count)
