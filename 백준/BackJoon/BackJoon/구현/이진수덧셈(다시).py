# 이 개사기 스킬을 알아두기

t = int(input())

for _ in range(t):
    nums = [int(e, 2) for e in input().split()]
    print(bin(sum(nums))[2:])





    