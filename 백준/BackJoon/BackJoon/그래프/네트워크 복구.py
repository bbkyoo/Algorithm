import sys
import heapq

inf = sys.maxsize

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dp = [inf]*(n+1)
    ck = [0]*(n+1)
    dp[start] = 0

    while heap:
        wei, now = heapq.heappop(heap)
        for w, next_node in matrix[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                ck[next_node] = now
                heapq.heappush(heap, (next_wei, next_node))

    return ck

n, m = map(int, input().split())

matrix = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a].append([c, b])
    matrix[b].append([c, a])

ck = dijkstra(1)
print(n-1)
for i in range(2, n+1):
    print(i, ck[i])


#먼저, '복구할 회선의 갯수' 를 구해보자. 이 갯수는 무조건 N - 1 개가 된다. 왜냐하면 N개의 컴퓨터가 있는데, 이 N개의 컴퓨터를

#연결하기 위해서는 최소 N - 1개의 회선이 필요하기 때문이다. 즉 ! 복구할 회선의 갯수 K 는 N - 1 값이 된다.

#그리고 그 복구한 회선의 정보를 표현해야한다. 이 부분을 위해서 본인은 'int Parent[]' 라는 배열을 하나 사용해주었다.

#다익스트라 알고리즘을 구현할 때, 값이 갱신되는 과정(방문하려는 정점에 드는 비용이 지금 계산하는 비용보다 더 비싼경우)에서

#값이 갱신된다면, Parent의 값을 설정해 주었다.

#예를 들어서 1번정점에서 2번정점으로 가는데 걸리는 시간이 10초였는데, 1번정점에서 3번정점을 통해 2번정점으로 가는데 걸리는 시간이 5초가 된다면, 
#이 때 다익스트라 알고리즘에서는 값의 갱신이 발생한다. 그럼 이 경우에 ! 2번정점의 부모값을 '3번'정점으로 바꿔주는 것이다. 이와 같은 방식을 이용해서 구현하였다.

#출처: https://yabmoons.tistory.com/444 [얍문's Coding World..]