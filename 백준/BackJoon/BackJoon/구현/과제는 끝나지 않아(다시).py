from collections import deque

stack = deque()
time = deque()
answer = deque()

n = int(input())

for i in range(n):
    x = list(map(int, input().split()))

    if x[0] == 1:
        stack.append(x[1])
        time.append(x[2])

    if time:
        time[-1] -= 1
        if time[-1] == 0:
            time.pop()
            answer.append(stack.pop())

print(sum(answer))
















