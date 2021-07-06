from collections import deque

a,b,c = map(int, input().split())
visited = [[0]*1501 for _ in range(1501)]
total = a + b + c

def bfs():
    global a,b,c
    q = deque()
    q.append([a,b])
    visited[a][b] = 1

    while q:
        a, b = q.popleft()
        c = total - a - b
        if a == b == c:
            return 1

        for na, nb in ((a,b),(a,c),(b,c)):
            if na < nb:
                nb -= na
                na += na

            elif na > nb:
                na -= nb
                nb += nb

            else:
                continue
    
            nc = total - na - nb
            a = min(min(na,nb),nc)
            b = max(max(na,nb),nc)

            if visited[a][b] == 0:
                q.append((a,b))
                visited[a][b] = 1
    return 0

if total % 3 != 0:
    print(0)
else:
    print(bfs())
