import heapq

def solution(jobs):
    start = -1
    heap = []
    now = 0
    answer = 0

    i = 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))