def solution(phone_number):
    
    p_l = len(phone_number) - 4
    temp = list(phone_number)
    for i in range(p_l):
        temp[i] = '*'
        
    answer = ''
    for i in range(len(temp)):
        answer += temp[i]

    return answer

