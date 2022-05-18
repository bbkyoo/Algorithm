# 아래는 유클리드 호제법 사용한 것

def u(a, b):
    if b == 0:
        return a
    return u(b, a%b)

a, b = map(int, input().split())
g = u(a, b)
l = a*b // g

print("최대공약수 =", g)
print("최소공배수 =", l)
