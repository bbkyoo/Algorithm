n, d = map(int, input().split())

nums = []
for i in range(1, n+1):
    nums.append(i)

cnt = 0
for i in nums:
    temp = str(i)
    for j in range(len(temp)):
        if temp[j] == str(d):
            cnt += 1
    
print(cnt)