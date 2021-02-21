import sys

def fibonacci(n,lst):
    if n == 0:
        lst[0] += 1
        return 0
    elif n == 1:
        lst[1] += 1
        return 1
    else:
        return fibonacci(n-1, lst) + fibonacci(n-2, lst)

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    lst = [0,0]
    fibonacci(N, lst)
    print(lst[0], lst[1])

