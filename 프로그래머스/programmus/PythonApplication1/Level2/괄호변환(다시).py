def divide(p):
    cnt1 = 0
    cnt2 = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 == cnt2: 
            index = i
            break

    return p[:index+1], p[index+1:] 


def isRight(u):
    q = []

    for i in range(len(u)):
        if len(q) == 0:
            q.append(u[i])
        elif u[i] == ")":
            q.pop()
        else:
            q.append(u[i])

    if len(q) == 0:
        return True
    else:
        return False

def solution(p):

    # 과정1
    if not p:
        return ""

    # 과정2
    u,v = divide(p)

    # 과정3
    if isRight(u):
        return u + solution(v)
    
    # 과정4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for i in range(1, len(u)-1):
            if u[i] == "(":
                answer += ")"
            else:
                answer += "("

        return answer








































