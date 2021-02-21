# 본 문제는 이전의 수 찾기 문제와 유사한 것을 확인할 수 있습니다.
# M 집합에 있는 요소들이 N 집합에 몇 개가 있는치를 출력하는 문제입니다.
# 시간을 해결하기 위한 문제이므로 단순히 list의 메소드인 count를 통해서 문제를 해결하는 것은 적절하지 않은 방법일 것입니다.
# 시간 복잡도를 줄이는 핵심 부분은 리스트 N에 요소가 몇 개 있는지 숫자를 세는 것입니다.

import sys

input = sys.stdin.readline

_ = int(input())
N = list(map(int , input().split()))
N.sort()

_ = int(input())
M = list(map(int , input().split()))

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)


n_dic = {}

for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))




























