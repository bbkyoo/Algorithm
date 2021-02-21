# 문자열 계산에서 eval() 함수는 문자열로 수식된 계산을 할때 사용된다.

def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))

    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n+1, e) for e in expression.split("*")]))

    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e) for e in expression.split("+")]))

    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e) for e in expression.split("-")]))

    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ("*", "-" , "+" ),
        ("*", "+" , "-" ),
        ("+", "-" , "*" ),
        ("+", "*" , "-" ),
        ("-", "*" , "+" ),
        ("-", "+" , "*" )
    ]

    for i in priorities:
        res = int(calc(i, 0, expression))
        answer = max(answer, abs(res))

    return answer




