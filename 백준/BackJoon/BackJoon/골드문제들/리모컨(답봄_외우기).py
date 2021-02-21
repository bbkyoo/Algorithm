#case 1
#- abs(N - 100)의 값을 구한다. (채널 100번에서 +,- 버튼만 채널을 이동하는 것이다)

#case 2
#- 0번부터 1,000,000까지 브루트 포스를 진행한다. 
#(이동하려고 하는 채널의 최댓값이 500,000 이기 때문에 500,000 보다 크면서 모든 숫자의 경우의 수를 거치는 1,000,000까지를 범위로 잡았다.

import sys
input = sys.stdin.readline

def check(num):
    num = list(str(num))
    for i in num:
        if i in s: 
            return False
    return True

n = int(input())
m = int(input())
s = list(input().strip())
result = abs(n-100)

for i in range(1000001):
    if check(i): 
        result = min(result, len(str(i)) + abs(i - n)) # 횟수는 해당 채널에서 +나 -를 누르는 횟수 = abs(i - n) 와 해당 채널을 누르는 횟수 = len(str(i))

print(result)
    

