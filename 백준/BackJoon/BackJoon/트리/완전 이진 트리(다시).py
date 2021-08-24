def solution(start, end, level):
    if start == end:
        ans[level].append(tree[start])
        return

    center = (start + end) // 2
    ans[level].append(tree[center])
    solution(start, center-1, level+1)
    solution(center+1, end, level+1)

k = int(input())
tree = list(map(int, input().split()))
ln = len(tree)
ans = [[] for _ in range(k)]

solution(0, ln-1, 0)
for a in ans:
    print(*a)