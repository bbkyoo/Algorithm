n = int(input())
k = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

if k >= n:
    print(0)
else:
    distance = []
    for i in range(1, len(sensor)):
        distance.append(sensor[i] - sensor[i-1])
    
    distance.sort()
    for _ in range(k-1):
        distance.pop()

    print(sum(distance))