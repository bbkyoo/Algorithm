def convert(s):
    s_tp = ""

    for i in range(len(s)):
        if s[i] != '0':
            s_tp += s[i]

    s_ln = len(s_tp)
    twice = []

    while True:
        if s_ln != 1: 
            twice.append(s_ln % 2)    
            s_ln = s_ln // 2
        else:
            twice.append(s_ln % 2)
            break

    twice.reverse()
    result = ''
    for i in twice:
        result += str(i)

    return result

def solution(s):
    count_zero = 0
    count = 0
    while True:
        for i in range(len(s)):
            if s[i] == '0':
                count_zero += 1

        if len(s) == 1 and s[0] == '1':
            break
        s = convert(s)
        count += 1

    answer = [count, count_zero]
    return answer









