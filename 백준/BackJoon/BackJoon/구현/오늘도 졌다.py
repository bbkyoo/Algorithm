import sys

input = sys.stdin.readline

first = list(map(int, input().split()))
second = list(map(int, input().split()))

isTrue = True
f_sm = 0
s_sm = 0
for i in range(len(first)):
    f_sm += first[i] 
    s_sm += second[i]

    if f_sm > s_sm:
        isTrue = False
        break

if isTrue:
    print("No")
else:
    print("Yes")

