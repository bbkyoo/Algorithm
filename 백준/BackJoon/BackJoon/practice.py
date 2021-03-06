import sys

input = sys.stdin.readline

s = list(input().rstrip())

q = []
stack = []

state = False
result = ""
for i in s:

    if i == "<":
        state = True
        q.append(i)
        while stack:
            result += stack.pop()

    elif i == ">":
        state = False
        q.append(i)
        while q:
            result += q.pop(0)

    elif i == " ":
        if state:
            q.append(i)
        else:
            while stack:
                result += stack.pop()
            result += " "

    else:
        if state:
            q.append(i)
        else:
            stack.append(i)

while stack:
    result += stack.pop()

print(result)




































