import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
result = [-1] * n 
stack = []

for i in range(n):
    while len(stack) != 0 and A[stack[-1]] < A[i]:  # 스택 맨 위의 값 A[stack[-1]] 보다 A[i]의 값이 더 클 경우 == 오 큰수의 정의
        result[stack.pop()] = A[i]
    stack.append(i)

for i in result:
    print(i, end=' ')