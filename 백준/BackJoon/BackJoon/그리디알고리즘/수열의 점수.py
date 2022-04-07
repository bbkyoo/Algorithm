n = int(input())

positive_nums = []
negative_nums = []
one = [] # 이 걸로 1을 굳이 빼는 이유는 1일 여러개 일 수도 있어서 이다.
for _ in range(n):
    num = int(input())
    if num > 1:
        positive_nums.append(num)
    elif num <= 0:
        negative_nums.append(num)
    else:
        one.append(num)

positive_nums.sort(reverse=True)
negative_nums.sort()

negative_sum = 0
if len(negative_nums) % 2 == 0:
    for i in range(0,len(negative_nums),2):
        negative_sum += negative_nums[i] * negative_nums[i+1]
else:
    if negative_nums:
        negative_sum += negative_nums.pop()
    for i in range(0,len(negative_nums),2):
        negative_sum += negative_nums[i] * negative_nums[i+1]

positive_sum = 0
if positive_nums:
    if len(positive_nums) % 2 == 0:
        for i in range(0,len(positive_nums),2):
            positive_sum += positive_nums[i] * positive_nums[i+1]
    else:
        if positive_nums:
            positive_sum += positive_nums.pop()
        for i in range(0,len(positive_nums),2):
            positive_sum += positive_nums[i] * positive_nums[i+1]

print(negative_sum + positive_sum + sum(one))