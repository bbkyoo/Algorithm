import heapq

def solution(heap, k):
    heapq.heapify(heap)

    count = 0
    while heap[0] < k and len(heap) > 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        if temp1 < k:
            temp = temp1 + (temp2 * 2)
            heapq.heappush(heap, temp)
            count += 1
        else:
            break

    for i in heap:
        if i < k:
            return -1 

    return count



