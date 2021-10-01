# 숫자는 중복가능하다.-> 중복 횟수에 제한이 없음 -> set으로 해결
# 비내림차순이다. -> 수열이 같거나 커지는 순이다. 정렬 이후 시작 index를 기준으로 
# 같은 index이거나 더 큰 index만 탐색한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
d = {}
out = []

def dfs(depth, n, m):
    if depth == m:
        temp = ' '.join(map(str, out))
        if temp not in d:
            d[temp] = 1
            print(temp)
        return

    for i in range(n):
        if depth == 0 or out[-1] <= arr[i]:
            out.append(arr[i])
            dfs(depth+1, n, m)
            out.pop()
            
dfs(0, n, m)