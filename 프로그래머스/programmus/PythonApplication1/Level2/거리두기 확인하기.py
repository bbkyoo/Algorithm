from collections import deque

def solution(places):
    def bfs(x, y, visited):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        q = deque([])
        q.append([x, y])
        visited[x][y] = 1

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(visited) and 0 <= ny < len(visited[0]):
                    if visited[nx][ny] == 0:
                        if place[nx][ny] == 'O':
                            visited[nx][ny] = visited[x][y] + 1
                            q.append([nx, ny])
                        elif place[nx][ny] == 'P':
                            if visited[x][y] <= 2:
                                return 0
                            else:
                                visited[nx][ny] = 1
                                q.append([nx, ny])
        return 1       

    answer = []
    for place in places:
        visited = [[0]*len(place[i]) for i in range(len(place))]
        ret = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P' and visited[i][j] == 0:
                    ret.append(bfs(i, j, visited))

        if 0 in ret:
            answer.append(0)
        else:
            answer.append(1)
    
    return answer


