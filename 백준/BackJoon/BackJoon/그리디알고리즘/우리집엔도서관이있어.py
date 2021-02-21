#결국 이 문제는 가장 큰 수에서부터 위로 올라가며
#가장 긴 증가수열을 찾아서 n에서 빼주면 된다.

import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

mx = n
for i in range(n-1,-1,-1):
    if nums[i] == mx:
        mx -= 1

print(mx)

