n = int(input())

s = []

for _ in range(n):
    s.append(input())

dic = {}

for i in s:
    k = len(i) - 1
    for j in i:
        if j in dic:
            dic[j] += pow(10, k)
        else:
            dic[j] = pow(10, k)
        k -= 1

nums = []

for value in dic.values():
    nums.append(value)

nums.sort(reverse=True)

result = 0
t = 9

for i in range(len(nums)):
    result += nums[i]*t