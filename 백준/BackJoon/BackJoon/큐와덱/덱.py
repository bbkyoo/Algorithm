import sys
from collections import deque 

N = int(sys.stdin.readline())
q = deque([])

for _ in range(N):
    s = sys.stdin.readline().split()
    if 'push_front' in s:
        q.appendleft(int(s[1]))
    elif 'push_back' in s:
        q.append(int(s[1]))
    elif 'pop_front' in s:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif 'pop_back' in s:
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif 'size' in s:
        print(len(q))
    elif 'empty' in s:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in s:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif 'back' in s:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])






