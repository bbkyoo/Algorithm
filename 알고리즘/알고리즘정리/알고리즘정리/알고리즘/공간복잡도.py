#예제1 공간 복잡도 O(1)

def factorial1(n):
    fac = 1
    for i in range(2, n+1):
        fac = fac * i
    return fac

#예제2 공간 복잡도 O(n)
def factorial2(n):
    if n > 1:
        return n * factorial2(n-1)
    else:
        return 1
