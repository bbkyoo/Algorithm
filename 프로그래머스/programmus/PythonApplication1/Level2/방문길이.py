def solution(dirs):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    d = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    x = 0
    y = 0
    answer = 0
    visited = set()

    for dir in dirs:
        i = d[dir]
        nx = x + dx[i]
        ny = y + dy[i]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in visited:
                visited.add((x, y, nx, ny))
                visited.add((nx, ny, x, y))
                answer += 1

        else:
            continue

        x, y = nx, ny

    return answer 