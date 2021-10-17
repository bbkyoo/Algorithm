import sys
import heapq

input = sys.stdin.readline

def cal(chair_idx):
    # 의자 번호 인덱스를 통해 의자 방문 횟수 계산
    global ans

    for i in range(len(chair_idx)):
        cidx = chair_idx[i]
        seated[cidx] += 1 
        if seated[cidx] == 2:
            ans += 1

r, c = map(int, input().split())

matrix = []
for _ in range(r):
    matrix.append(list(input().strip()))

chair = []
people = []
seated = [0] * 10000
finished = [0] * 10000
ans = 0
chair_idx = []
heap = []
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'X':
            people.append([i, j])
        elif matrix[i][j] == 'L':
            chair.append([i, j])

# 각 사람과 의자 사이의 거리, 사람 인덱스, 의자 인덱스를 우선순위큐에 넣어준다.
for i, person in enumerate(people): 
    px, py = person[0], person[1]
    for j, ch in enumerate(chair):
        cx, cy = ch[0], ch[1]
        dist = (px - cx)**2 + (py - cy)**2
        heapq.heappush(heap, (dist, i, j))

# 최소 1개의 의자와 1명의 사람이 있기 때문에 미리 한번 heappop을 해준다.
dist, psx, chx = heapq.heappop(heap) 
chair_idx.append(chx)  # chair_idx에 값이 들어갔다는 것은 어떤 사람이 의자를 방문하는 경우

finished[psx] = 1

while heap:
    nd, np, nc = heapq.heappop(heap)
    if dist != nd: # 거리가 이전 것과 다르면
        dist = nd # 거리변경
        if chair_idx: # 기존에 계산하지 않은 의자 인덱스가 남아있으면
            cal(chair_idx) # 의자 인덱스를 가지고 의자 방문 계산
            chair_idx.clear()
    if not seated[nc] and not finished[np]: # 아직 방문하지 않은 의자가 있고 그 사람이 한번도 어떤 의자를 방문한적 없으면
        chair_idx.append(nc) # 의자 인덱스 추가
        finished[np] = 1 # 사람 인덱스 True로 변경

if chair_idx: # 남아있는 계산되지 않은 의자 인덱스가 있으면
    cal(chair_idx) # 계산

print(ans)