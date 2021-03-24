from collections import deque

def update_info():
    for p in range(len(pole_info)):
        pole_info[p][0] = array[p][6]
        pole_info[p][1] = array[p][2]

t = int(input())

array = []
for _ in range(t):
    array.append(deque(map(int, input())))

pole_info = list(map(lambda x: [x[6], x[2]], array))
rotate_info = [0]*t

k = int(input())

for _ in range(k):
    num, direction = map(int, input().split())

    rotate_info[num-1] = direction
    
    if num != 1:
        for i in range(num-2, -1, -1):
            if pole_info[i][1] == pole_info[i+1][0]:
                break
            else:
                rotate_info[i] = -(rotate_info[i+1])

    if num != t:
        for i in range(num, t):
            if pole_info[i][0] == pole_info[i-1][1]:
                break
            else:
                rotate_info[i] = -(rotate_info[i-1])

    for i in range(t):
        array[i].rotate(rotate_info[i])

    update_info()
    for i in range(t):
        rotate_info[i] = 0

answer = 0
for i in range(len(array)):
    if array[i][0] == 1:
        answer += 1

print(answer)




















