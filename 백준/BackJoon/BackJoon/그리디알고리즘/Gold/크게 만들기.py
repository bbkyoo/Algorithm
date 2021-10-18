import sys

#input = sys.stdin.readline

#N, K = map(int, input().split())

#nums = list(input().strip())
#nums_st = sorted(nums)

#for i in range(K):
#    if nums_st[i] in nums:
#        del nums[nums.index(nums_st[i])]

#result = ''
#for i in range(len(nums)):
#    result += str(nums[i])

#print(result)

input = sys.stdin.readline
n, k = map(int, input().split())
s = list(input().strip())
t = []
tk = k

for i in range(n):
    while tk > 0 and t and t[-1] < s[i]: # 이 알고리즘이 중요!, k만큼 앞에서 부터 작은 것을 거르고 남은 것 들만을 t에 더하여 출력, 이 것이 더 시간복잡도가 낮아진다.  
        del t[-1]
        tk -= 1
    t.append(s[i])

print(''.join(t[:n-k]))
print(t)






