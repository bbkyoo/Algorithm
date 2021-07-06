# https://coder38611.tistory.com/115

t = int(input())

for _ in range(t):
    n = int(input())
    button = [0]*5    
    sixties, tens, ones = n//60, (n%60)//10, n%10

    if ones > 5:
        tens += 1
        ones -= 10
    if tens > 3:
        sixties += 1
        tens -= 6
    if tens < 0 and ones == 5:
        tens += 1
        ones -= 10

    button[0] = sixties
    button[2-(tens >= 0)] = abs(tens) # (tens >= 0) 이것은 조건문으로 True이면 1 False이면 0
    button[4-(ones >= 0)] = abs(ones)
    print(*button)
    