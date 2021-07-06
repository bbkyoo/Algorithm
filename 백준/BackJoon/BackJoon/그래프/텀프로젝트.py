import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global result

    cycle.append(x)
    visited[x] = 1
    number = numbers[x]
    
    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

t = int(input())

for _ in range(t):
    n = int(input())
    numbers =  [0] + list(map(int ,input().split()))
    visited = [1] + [0]*n
    result = []

    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)
    
    print(n - len(result))





