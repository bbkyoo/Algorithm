# https://velog.io/@sch804/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1339%EB%B2%88-%EB%8B%A8%EC%96%B4-%EC%88%98%ED%95%99

N = int(input())

s = []

for _ in range(N):
    s.append(input()) 
    
dic = {}


for i in s:
    k = len(i)-1
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
    t -= 1

print(result)