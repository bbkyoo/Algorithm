# 2개의 괄호와 그의 대한 각각의 값이 있었을때 풀 수 있는 알고리즘, 꼭! 다시해보기

s = list(input())
q = []

for i in s:
    if i == ')':
        t = 0
        while q:
            top = q.pop()
            if top == '(':
                if t == 0:
                    q.append(2)
                else:
                    q.append(2 * t)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                t = t + int(top)
    
    elif i == ']':
        t = 0
        while q:
            top = q.pop()
            if top == '[':
                if t == 0:
                    q.append(3)
                else:
                    q.append(3 * t)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                t = t + int(top)
    
    else:
        q.append(i)

result = 0
for i in q:
    if i == "(" or i == "[":
        result = 0
        break
    else:
        result += i

print(result)