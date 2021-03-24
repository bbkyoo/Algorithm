#신호등에 도착한 시간 % ( 빨간불 + 초록불 ) 의 값이 빨간불보다 작거나 같으면 빨간불, 크다면 초록불이라는 것을 알 수 있다.

n, l = map(int, input().split())
t = 0
pre = 0

for _ in range(n):
    d, r, g = map(int, input().split())
    
    # t - 위치 d에 있는 신호등까지 걸린 시간
    t += d - pre
    pre = d

    red = t % (r + g)

    if red <= r:
        t += r - red

print(t + (l - pre))
