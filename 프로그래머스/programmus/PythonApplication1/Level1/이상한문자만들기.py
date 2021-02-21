def solution(s):
    
    answer = ''
    idx = 0

    for i in s:
        if i.isalpha(): # 이것이 알파벳인지 구분하는 함수가 있다.
            idx += 1
            if idx % 2 != 0:
                answer += i.upper() # 이게 한 글자에도 가능하다.
            else:
                answer += i.lower() # 이게 한 글자에도 가능하다.
        else:
            idx = 0
            answer += ' '           

    return answer

