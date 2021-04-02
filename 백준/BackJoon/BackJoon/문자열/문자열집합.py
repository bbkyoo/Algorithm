# 문자열은 일치하는 것을 찾을 때 딕셔너리 사용
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = {input().rstrip() for _ in range(n)}

count = 0
for _ in range(m):
    temp = input().rstrip()
    if temp in arr:
        count += 1

print(count)