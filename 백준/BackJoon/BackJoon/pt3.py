import sys
sys.setrecursionlimit(10**6)

def solution(n, info):
    def solve(depth, n):
        nonlocal result
        nonlocal mx
    
        if depth == n:
            temp1 = 0
            temp2 = 0

            for i in range(len(visited)):
                if visited[i] > info[i]:
                    temp1 += 10-i
                elif visited[i] <= info[i] and info[i] != 0:
                    temp2 += 10-i

            if temp1 > temp2:
                if temp1 > mx:
                    mx = max(mx, temp1)
                    result = []
                    result.append(visited.copy())
                elif temp1 == mx:
                    result.append(visited.copy())
            return

        for i in range(len(visited)):
            if visited[i] <= info[i]:
                visited[i] += 1
                solve(depth+1, n)
                visited[i] -= 1

    visited = [0] * len(info)
    result = []
    mx = 0
    solve(0, n)
    if len(result) == 0:
        return [-1]
    else:
        temp = []
        for i in result:
            if i not in temp:
                temp.append(i)

        temp.sort(key = lambda x : (x[10], x[9], x[8], x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0]))
        return temp[-1]
