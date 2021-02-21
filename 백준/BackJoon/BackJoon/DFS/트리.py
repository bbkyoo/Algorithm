def dfs(v):
    global cnt

    isTrue = False # 이 방법 기억해두기

    visited[v] = 1
    
    for i in range(n):
        if visited[i] == 0 and tree[v][i] == 1:
            isTrue = True
            dfs(i)
    if isTrue == False:
        cnt += 1

n = int(input())
parent_tree = list(map(int, input().split()))
remove = int(input())
tree = [[0]*n for i in range(n)]
visited = [0] * n
root = 0

for i in range(n):
    if parent_tree[i] == -1:
        root = i
        continue
    tree[parent_tree[i]][i] = 1
    tree[i][parent_tree[i]] = 1

for i in range(n):
    tree[i][remove] = 0
    tree[remove][i] = 0


cnt = 0
dfs(root)

if root == remove:
    print(0)
else:
    print(cnt)