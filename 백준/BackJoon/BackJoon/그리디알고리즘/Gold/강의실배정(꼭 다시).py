# 방법 1

#import sys
#from queue import PriorityQueue

#def solution():
#    pque = PriorityQueue()
#    pque.put((-time[0][1],time[0][1]))
#    for i in range(1, N):
#        if pque.queue[-1][1] <= time[i][0]:
#            pque.get()
#            pque.put((-time[i][1],time[i][1]))
#        else:
#            pque.put((-time[i][1],time[i][1]))

#    print(pque.qsize())
#    return

#input = sys.stdin.readline

#N = int(input())

#time = []

#for _ in range(N):
#    s, t = map(int, input().split())
#    time.append([s,t])

#time.sort(key=lambda x: x[0])

#solution()


# 방법 2

import sys
import heapq

input = sys.stdin.readline

n = int(input())

time = []

for _ in range(n):
    s, t = map(int, input().split())
    time.append([s, t])

time.sort(key = lambda x : x[0])

heap = []

for i in range(n):
    if len(heap) != 0 and heap[0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))


# 방법 3

#import sys

#input = sys.stdin.readline

#n = int(input())
#time = []
#end = [0]

#for i in range(n):
#    time.append((list(map(int, input().split()))))
#time.sort(key = lambda x: (x[0],x[1]))

#for i in range(n):
#    if time[i][0] >= min(end):
#        end.remove(min(end))
#        end.append(time[i][1])
#    else:
#        end.append(time[i][1])

#print(len(end))





