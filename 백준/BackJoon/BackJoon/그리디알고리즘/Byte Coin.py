import sys

input = sys.stdin.readline 

n, w = map(int, input().split())

s = []
for _ in range(n):
    s.append(int(input()))

current = [s[0]]

for i in range(1, n):
    if current[-1] <= s[i]:
        current.append(s[i]) 
    else:
        if len(current) == 1:
            current = [s[i]]
        else:
            count = w // current[0]
            w = w % current[0]
            w += (count * current[-1])
            current = [s[i]]

if len(current) > 1:
    count = w // current[0]
    w = w % current[0]
    w += (count * current[-1])
    
print(w)
