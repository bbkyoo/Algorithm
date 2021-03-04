a, b = map(int, input().split())

nums = []

num = 1
for _ in range(b):
    if nums.count(num) != num:
        nums.append(num)
    else:
        num += 1
        nums.append(num)

print(sum(nums[a-1:b]))