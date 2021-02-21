def solution(s):
    s = s.lower()
    l = s.split(" ") # 여기에 list split() 쓰면 안됌

    result = ''
    for i in l:
        result += i.capitalize()
        result += ' '
       
    return result[:-1]

