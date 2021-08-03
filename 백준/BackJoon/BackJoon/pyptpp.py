def solution(p):
    def isgalho(s):
        answer = []
        for i in s:
            if len(answer) == 0:
                answer.append(i)
            else:
                if answer[-1] == "(":
                    if i == ")":
                        answer.pop()
                    else:
                        answer.append(i)

        if answer:
            return False
        else:
            return True


    def dfs(w):
        if len(w) == 0:
            return ""

        u = ""
        v = ""

        for i in range(len(w)):
            if len(u) == 0:
                u += w[i]
            else:
                if u.count('(') == u.count(')'):
                    v += w[i:]
                    break
                else:
                    u += w[i]

        if isgalho(u):
            return u + dfs(v)
        else:
            u = list(u)
            for i in range(len(u)):
                if u[i] == ')':
                    u[i] = "("
                elif u[i] == '(':
                    u[i] = ")"

            u = ''.join(u)
        return "(" + dfs(v) + ")" + u[1:-1]

    return dfs(p)