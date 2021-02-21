from collections import deque

def check_right(start, dirs):
    # 더 이상 조사가 불가능한 경우
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return

    # 오른쪽 확인
    if gears[start-1][2] != gears[start][6]:
        # 인접한 톱니바퀴가 회전 가능한지부터 먼저 파악한다.
        check_right(start+1, -dirs)
        # 회전 시킨다.
        gears[start].rotate(dirs)

def check_left(start, dirs):
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return

    # 왼쪽 확인
    if gears[start+1][6] != gears[start][2]:
        check_left(start-1, -dirs)
        gears[start].rotate(dirs)

gears = {}    

# 기준 톱니바퀴가 있을때, 왼쪽과 맞닿는 지점은 idx2, 오른쪽은 6이다.
for i in range(1, 5):
    gears[i] = deque(list(map(int, input())))

n = int(input())

for _ in range(n):
    num, dirs = map(int, input().split())

    check_right(num+1, -dirs)
    check_left(num-1, -dirs)

    gears[num].rotate(dirs)

result = 0

for i in range(4):
    result += (2**i) * gears[i+1][0]
print(result)




















