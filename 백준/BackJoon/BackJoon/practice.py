def rotate(s, n):
    return s[n:] + s[:n]

def solution(s):
    s = list(s)
    answer = 0
    for i in range(len(s)):
        s1 = rotate(s, i)
        isTrue = True
        temp = []
        for j in s1:
            if temp:
                top = temp[-1]
                if top == '[':
                    if j == ']': 
                        temp.pop()
                    elif j == '}' or j == ')':
                        isTrue = False
                        break
                    else:
                        temp.append(j)

                elif top == '(':
                    if j == ')': 
                        temp.pop()
                    elif j == ']' or j == '}':
                        isTrue = False
                        break
                    else:
                        temp.append(j)

                elif top == '{':
                    if j == '}': 
                        temp.pop()
                    elif j == ')' or j == ']':
                        isTrue = False
                        break
                    else:
                        temp.append(j)
            else:
                temp.append(j)

        if temp:
            continue
        else:
            if isTrue:
                answer += 1

    return answer

