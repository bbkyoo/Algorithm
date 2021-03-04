# 버블은 연속된 두 원소를 검사하여 정렬
# 선택은 최솟값을 선택해서 맨앞으로 보내고 하는 정렬

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = int(input())

# 이건 선택한 버블정렬이다. 
# 버블정렬은 내부 반복문이 끝날 때마다 자리 하나가 고정이 된다.
# https://wayhome25.github.io/cs/2017/04/16/cs-17/ 버블정렬과, 선택정렬, 삽입정렬 정리
# https://www.daleseo.com/sort-insertion/ 이건 삽입정렬

for i in range(n-1):
    if s == 0:
        break

    mx, idx = a[i], i
    for j in range(i+1, min(n, i+1+s)):
        if mx < a[j]:
            mx = a[j]
            idx = j

    s -= idx - i

    for j in range(idx, i, -1):
        a[j] = a[j-1]

    a[i] = mx

print(' '.join(map(str, a)))

