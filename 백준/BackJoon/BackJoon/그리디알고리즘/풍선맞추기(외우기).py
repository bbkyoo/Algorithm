# 높이 a의 풍선을 볼 때, a+1 높이에서 날아오는 화살이 있는지 검사해주자!
# 이런 문제는 인덱스에서 검사해 주는 문제이다

import sys

input = sys.stdin.readline

n = int(input())

h = list(map(int, input().split()))
cnt = [0] * 1000001
count = 0

for i in range(n):
    if not cnt[h[i]+1]:
        cnt[h[i]] += 1
        count += 1
    else:
        cnt[h[i]+1] -= 1
        cnt[h[i]] += 1

print(count)

