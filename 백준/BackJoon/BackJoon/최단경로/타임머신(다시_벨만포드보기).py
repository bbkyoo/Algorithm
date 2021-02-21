# 최단 경로에서는 다익스트라 알고리즘을 사용했었는데, 비슷하지만
# 가중치가 음수일 때는 사용이 불가능하므로, 벨만-포드 알고리즘을 쓴다.

# 1. graph를 우선순위 힙이 아닌, 일반 배열로 받는다. (일반적 w 누적이랑 다름)
# 2. 다음 정점 > nw + w가 아닌, 다음 정점 > 이전 정점 + w로 접근한다.
# 3. 계속 줄어드는지 보기 위해 n번 반복을 한다.
# 4. 계속 줄어든다면(n번째 까지 값이 갱신된다면), minus=True한다.
# 5. minus라면 -1, 아니라면 정점의 값을 출력한다. (없으면 -1)

N, M = map(int , input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
bf = [1e9] * (N+1)

def solve_bf():
    bf[1] = 0
    minus = False
    for i in range(N):
        for j in range(M):
            v = matrix[j][0]
            nv = matrix[j][1]
            w = matrix[j][2]
            if bf[v] != 1e9 and bf[nv] > bf[v] + w:
                bf[nv] = bf[v] + w
                if i == N-1:
                    minus = True

    if minus:
        print(-1)

    else:
        for i in range(2, N+1):
            if bf[i] == 1e9:
                print(-1)
            else:
                print(bf[i])
solve_bf()
