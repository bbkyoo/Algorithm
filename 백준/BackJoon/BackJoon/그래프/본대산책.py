# 0 : 정보과학관
# 1 : 전산관
# 2 : 신앙관
# 3 : 미래관
# 4 : 진리관
# 5 : 환경직기념관
# 6 : 학생회관
# 7 : 형남공학관

# https://data-make.tistory.com/401
# 정보과학관 = n분 후 전산관으로 도착할 수 있는 상태 + n분 후 미래관으로 도착할 수 있는 상태가 되고,
# 전산관 = n분 후 정보과학관으로 도착할 수 있는 상태 + n분 후 신앙관으로 도착할 수 있는 상태 + n분 후 미래관으로 도착할 수 있는 상태가 된다.
import sys

dp = [1,0,0,0,0,0,0,0]

def move(state):
    temp = [0 for _ in range(8)]
    temp[0] = state[1] + state[3]
    temp[1] = state[0] + state[2] + state[3]
    temp[2] = state[1] + state[3] + state[4] + state[5]
    temp[3] = state[0] + state[1] + state[2] + state[5]
    temp[4] = state[2] + state[5] + state[6] 
    temp[5] = state[3] + state[2] + state[4] + state[7]
    temp[6] = state[4] + state[7] 
    temp[7] = state[5] + state[6]

    for i in range(8):
        temp[i] %= 1000000007

    return temp

for i in range(int(input())):
    dp = move(dp)

print(dp[0])




