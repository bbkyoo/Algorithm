# https://kimmeh1.tistory.com/258

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0] * (v+1)
parent = [[0 for _ in range(21)] for _ in range(v+1)]
visited = [False] * (v+1)