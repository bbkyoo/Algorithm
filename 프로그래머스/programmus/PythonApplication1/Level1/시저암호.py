def solution(s, n):
    arr = []
    
    somun = 'qwertyuioplkjhgfdsazxcvbnm'
    for i in range(len(s)):
        if s[i] == ' ':
            arr.append(' ')
        else:
            temp = ord(s[i])+n
            if ord(s[i])+n > 122 :
                temp -= 26
            elif ord(s[i])+n > 90 and s[i] not in somun:
                temp -= 26
            arr.append(temp)

    answer = ''
    for i in range(len(arr)):
        if arr[i] == ' ':
            answer += ' '
        else:
            answer += chr(arr[i])

    return answer



