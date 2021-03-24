# 부동소수점 오류 주의!! 이걸 해결하려면 1000을 곱해서 정수형으로 만들어준다
import sys
import decimal

input = sys.stdin.readline

def gersa(temp1, n, k):    

    while k and temp1:
        temp1.pop(0)
        temp1.pop()
        k -= 1

    sm = sum(temp1)
    result = round(sm / len(temp1), 2)

    return result

def bojung(temp2, n, k):
    tk = k

    while tk and temp2:
        temp2.pop(0)
        temp2.pop()
        tk -= 1

    while tk < k:
        temp2.insert(0 ,temp2[0])
        temp2.append(temp2[-1])
        tk += 1

    sm = sum(temp2)
    result = round(sm / len(temp2), 2)

    return result


n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(float(input()))

arr.sort()
temp1 = arr.copy()
temp2 = arr.copy()

result1 = gersa(temp1, n, k)
result2 = bojung(temp2, n, k)

print('%.2f'%result1)
print('%.2f'%result2)













