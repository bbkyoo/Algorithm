import sys

input = sys.stdin.readline

k = int(input())
arr = [ list(map(int, input().split())) for _ in range(6)]

w = 0
h = 0
w_idx = 0
h_idx = 0

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            w_idx = i

    elif arr[i][0] == 3 or arr[i][0] == 4:
        if h < arr[i][1]:
            h = arr[i][1]
            h_idx = i

sub_w = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1]) # 가장 긴 가로변 양옆에 붙어있는 세로변들의 차이
sub_h = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1]) # 가장 긴 세로변 양옆에 붙어있는 가로변들의 차이

print(((w*h) - (sub_w*sub_h)) * k)