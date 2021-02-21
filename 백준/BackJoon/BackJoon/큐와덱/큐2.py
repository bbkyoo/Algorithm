import sys
from collections import deque # 이걸 사용해서 시간복잡도를 줄인다.

n = int(sys.stdin.readline())

queue = deque([]) # 큐는 이렇게 선언을 한다.

for _ in range(n):
    temp = sys.stdin.readline().split()
    if 'push' in temp:
        queue.append(int(temp[1]))
    elif 'pop' in temp:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft()) # 이렇게 하면 왼쪽을 출력하고 없앤다.
    elif 'size' in temp:
        print(len(queue))
    elif 'empty' in temp:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in temp:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in temp:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

