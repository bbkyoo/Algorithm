import sys
N = int(sys.stdin.readline())
lst = [0] * 10001
for i in range(N):
    lst[int(sys.stdin.readline())] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)

# 이 문제에서 핵심은 인덱스의 수를 값으로 받고 그 인덱스의 수만큼 인덱스를 출력하는 것이다.

