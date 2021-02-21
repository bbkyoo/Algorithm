def solution(s):
    
    answer = False

    s = s.lower()
    
    c_p = 0
    c_y = 0

    if ('p' not in s ) and ('y' not in s):
        return True

    for i in range(len(s)):
        if s[i] == 'p':
            c_p += 1
        elif s[i] == 'y':
            c_y += 1
     
    if c_p == c_y :        
        answer = True

    return answer

