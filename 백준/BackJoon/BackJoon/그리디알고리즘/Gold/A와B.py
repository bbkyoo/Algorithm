#문자열의 뒤에 A를 추가한다.
#문자열을 뒤집고 뒤에 B를 추가한다.
# S를 T로 변경하고자 한다면 로직을 생각하기 어렵지만, T를 S로 변경하면 쉽게 풀리는 문제이다.

import sys

input = sys.stdin.readline 

s = list(input().strip())
t = list(input().strip())
result = 0

while True:
    if len(s) == len(t):
        if s == t:
            result = 1
        break
    
    if t[-1] == "A":
        t.pop()
    else:
        t.pop()
        t.reverse()

print(result)
        