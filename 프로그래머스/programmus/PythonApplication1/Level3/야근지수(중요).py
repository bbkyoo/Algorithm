import heapq

def solution(n, works):
    heap = []

    for work in works:
        heapq.heappush(heap, (-work, work))

    for i in range(n): # 힙은 이렇게 쓰는 거다
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-work, work))

    result = 0
    for i in heap:
        if i[1] > 0:
            result += i[1]**2

    return result



