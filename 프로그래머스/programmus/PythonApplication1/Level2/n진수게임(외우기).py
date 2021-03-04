def trans(n,num):
    arr = "0123456789ABCDEF"
    ret = ''
    if num == 0:
        return '0'
    while num > 0:
        ret = arr[num % n] + ret
        num = num // n

    return ret

def solution(n,t,m,p):
    answer = ""
    string = ""

    for i in range(t*m):
        string += trans(n, i)

    for s in range(p-1, t*m, m):
        answer += string[s]

    return answer





       
        













