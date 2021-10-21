# 어디가 틀렸을까? 

#import sys
#input = sys.stdin.readline

#s = list(input().strip())
#s.reverse()
#i = 0
#length = 0
#while i < len(s):
#    if s[i] == ')':
#        i += 1
#    elif s[i] == '(':
#        if i+1 < len(s):
#            length = length * int(s[i+1])
#            i += 2
#    else:
#        length += 1
#        i += 1

s = input()
stack = []
length = 0
temp = ''
for c in s:
    if c.isdigit():
        length += 1
        temp = c
    elif c == '(':
        stack.append((temp, length-1))
        length = 0
    else:
        mul, pre = stack.pop()
        length = (int(mul)*length) + pre

print(length)