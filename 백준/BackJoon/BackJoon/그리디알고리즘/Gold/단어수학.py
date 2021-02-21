# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
# ord('a') -> 97
# ord('0') -> 48
# pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
# pow(2, 4) -> 16
# pow(3, 3) -> 27

N = int(input())

ss = []

for _ in range(N):
    ss.append(input()) 

alphabet = [0 for i in range(26)]

for s in ss:
    i = 0
    while s:
        now = s[-1]
        alphabet[ord(now) - ord('A')] += pow(10, i)
        i += 1
        s = s[:-1]

alphabet.sort(reverse = True)
ans = 0
for i in range(9,0,-1):
    ans += i * alphabet[9 - i]
print(ans)

