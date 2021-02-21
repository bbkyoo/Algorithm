def solution(s):
    lt = s.split(" ")

    for i in range(len(lt)):
        lt[i] = int(lt[i])

    result = ''
    result += str(min(lt))
    result += ' '
    result += str(max(lt))
    
    return result

