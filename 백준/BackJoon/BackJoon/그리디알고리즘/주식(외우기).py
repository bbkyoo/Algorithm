import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    day = list(map(int, input().split()))
    day.reverse()
    sum = 0
    mx = 0
    
    for i in range(len(day)):
        if mx < day[i]:
            mx = day[i]
        else:
            sum += mx - day[i]

    print(sum)        