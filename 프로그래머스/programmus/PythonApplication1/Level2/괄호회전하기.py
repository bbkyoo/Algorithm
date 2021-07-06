def rotate(num, s):
    return s[num:] + s[:num]  

def isgalho(s):
    answer = True

    q = []
    for i in s:
        if i == ")":
            if q:
                t = q.pop()
                if t == '(':
                    continue
                else:
                    return False
            else:
                return False

        elif i == "]":
            if q:
                t = q.pop()
                if t == '[':
                    continue
                else:
                    return False
            else:
                return False
    
        elif i == "}":
            if q:
                t = q.pop()
                if t == '{':
                    continue
                else:
                    return False
            else:
                return False

        else:
            q.append(i)

    if len(q) == 0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        temp = rotate(i, s)
        if isgalho(temp):
            answer += 1

    return answer


























