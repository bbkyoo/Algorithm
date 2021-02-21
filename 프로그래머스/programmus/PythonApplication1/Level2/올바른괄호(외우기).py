#def solution(s):
#    cnt1 = 0
#    cnt2 = 0
#    for i in range(len(s)):
#        if s[i] == '(':
#            cnt1 += 1
#        elif s[i] == ')':
#            cnt2 += 1

#    if cnt1 != cnt2 or s[0] == ")" or s[-1] == "(":
#        return False
#    else:
#        temp1 = 0
#        temp2 = 0
#        for i in range(len(s)-1, -1, -1):
#            if i == 0:
#                if cnt1 == cnt2 + 1:
#                    return True
#                else:
#                    return False                

#            if s[i] == '(':
#                cnt1 -= 1
#                temp1 += 1
#            elif s[i] == ')':
#                cnt2 -= 1
#                temp2 += 1 

#            if temp1 > temp2:
#                return False

def solution(s):
    answer = True

    q = []

    for i in s:
        if i == "(":
            q.append('(')
        else:
            try:
               q.pop()
            except:
                return False

    if len(q) == 0:
        return True
    else:
        return False

print(solution("()()"))
