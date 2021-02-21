import sys

input = sys.stdin.readline

n, w, l = map(int, input().split())

truck = list(map(int, input().split()))

time = 0
q = [0]*w

while q:
    time += 1
    q.pop(0)
    if truck:
        if sum(q) + truck[0] <= l:
            q.append(truck.pop(0))
        else:
            q.append(0)

print(time)

                
