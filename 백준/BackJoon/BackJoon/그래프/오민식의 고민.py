import sys
inf = sys.maxsize

def check(e):
    visited = [0]*n
    q = [e]
    while q:
        a = q.pop()
        if a == t_e:
            return True
        visited[a] = 1
        for b, c in matrix[a]:
            if visited[b] == 0:
                q.append(b)
    return False

def BF():
    for i in range(n+1):
        if bf[t_e] == (-inf) and i == n:
            print('gg')
            return
        for j in range(n):
            if bf[j] == (-inf):
                continue
            for e, t in matrix[j]:
                if bf[j] + t > bf[e]:
                    bf[e] = bf[j] + t
                    if i == n:
                        if check(e):
                            print("Gee")
                            return False

    return True

n, t_s, t_e, m = map(int, input().split())
matrix = [[] for _ in range(n)]
bf = [(-inf)]*(n)

for _ in range(m):
    s, e, t = map(int, input().split())
    matrix[s].append([e, t])

t = list(map(int, input().split()))
bf[t_s] = t[t_s]

for i in range(len(t)):
    for j in range(len(matrix[i])):
        for k in range(len(t)):
            if matrix[i][j][0] == k:
                matrix[i][j][1] = t[k] - matrix[i][j][1]

if BF():
    print(bf[t_e])