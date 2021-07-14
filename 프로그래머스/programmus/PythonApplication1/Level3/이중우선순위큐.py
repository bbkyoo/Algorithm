import heapq

def solution(operations):
    heap = []
    for i in operations:
        if i == "D -1":
            if heap:
                heapq.heappop(heap)
        elif i == "D 1":
            if heap:
                heap.remove(max(heap))
        else:
            temp = i.split()
            heapq.heappush(heap, int(temp[1]))

    if heap:
        return [max(heap),min(heap)]
    else:
        return [0,0]