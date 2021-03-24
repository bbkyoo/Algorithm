from collections import deque

# pole_info(= 각 톱니바퀴의 왼쪽 오른쪽 극 정보)를 update 한다.
def update_pole_info():
    for p in range(t):
        pole_info[p][0], pole_info[p][1] = matrix[p][6], matrix[p][2]

t = int(input())

matrix = []
for _ in range(t):
    matrix.append(deque(map(int, input())))

 # 각 톱니바퀴의 왼쪽 오른쪽 극 정보
pole_info = list(map(lambda x : [x[6], x[2]], matrix)) # 이 스킬 기억하기 중요하고 유용함

# 0이면 회전X, 1이면 시계방향, -1이면 반시계방향으로 회전
rotate_info = [0]*t

k = int(input())

for _ in range(k):
    num, direction = map(int, input().split())
    
    rotate_info[num-1] = direction

    # num 톱니바퀴 기준, 왼쪽 톱니바퀴들을 회전시킬지 가만히둘지 결정한다.
    if num != 1:
        for i in range(num - 2, -1, -1):
            if pole_info[i][1] == pole_info[i+1][0]:
                break
            else:
                rotate_info[i] = -(rotate_info[i+1])

    # num 톱니바퀴 기준, 오른쪽 톱니바퀴들을 회전시킬지 가만히둘지 결정한다.
    if num != t:
        for i in range(num, t):
            if pole_info[i][0] == pole_info[i-1][1]:
                break
            else:
                rotate_info[i] = -(rotate_info[i-1])

    # 톱니바퀴 회전시킨다.
    for i in range(t):
        matrix[i].rotate(rotate_info[i])

    # 'pole_info', 'rotate_info' 정보를 초기화 한다.
    update_pole_info()
    for i in range(t):
        rotate_info[i] = 0

# 점수 구하기
answer = 0
for i in range(t):
    if matrix[i][0] == 1:
        answer += 1
print(answer)































