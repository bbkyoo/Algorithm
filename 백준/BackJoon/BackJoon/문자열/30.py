#30의 배수가 되는 조건

#- 일의 자리수가 0이여야 함.
#- 각 자리의 숫자들을 더했을때 3으로 나누어 떨어져야함.

n = list(map(int, input()))

n.sort(reverse = True)

if n[-1] != 0:
    print(-1)
elif sum(n) % 3 != 0:
    print(-1)
else:
    for i in n:
        print(i, end="")
