import sys
input = sys.stdin.readline

def dfs(start, depth):
    if depth == l:
        vo = 0
        co = 0
        for i in range(l):
            if arr[i] in 'aeiou':
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(arr))
        return

    for i in range(start, c):
        if check[i] == 0:
            arr.append(s[i])
            check[i] = 1
            dfs(i+1, depth+1)
            check[i] = 0
            arr.pop()

l, c = map(int, input().split())
arr = []
s = input().split()
s.sort()
check = [0]*(c)
dfs(0, 0)