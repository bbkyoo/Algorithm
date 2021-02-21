def solution(s):
 
    answer = False
    num = ['0','1','2','3','4','5','6','7','8','9']

    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] in num:
                answer = True
            else:
                answer = False
                break

    return answer


