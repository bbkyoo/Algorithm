from collections import deque

vec = [[0,1,3],[0,1,2,4],[1,2,5],[0,3,4,6],[1,3,4,5,7],[2,4,5,8],[3,6,7],[4,6,7,8],[5,7,8]]    

def bfs(s):
    q = deque([])
    check = "000000000"
    q.append("000000000")
    time = 1

    while q:
        size = len(q)
        while size:
            here = q.popleft()

            for i in range(9):
                next = here
                for j in range(len(vec[i])):
                    if next[vec[i][j]] == '1':
                        next[vec[i][j]] = '0'
                    else:
                        next[vec[i][j]] = '1'

                if check.find(next) != check[-1]:
                    continue

                if s == next:
                    return time
                q.append(next)
                check.insert(next)
            size -= 1

p = int(input())

for _ in range(p):
    matrix = []
    st = ""
    for _ in range(3):
        temp = list(input())
        matrix.append(temp)

        for i in temp:
            if i == '*':
                st += '1'
            else:
                st += '0'
        
    if st == "000000000":
        print('0')
    else:
        print(bfs(st))
                




