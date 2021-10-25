n, l = map(int, input().split())
t = 0
pre = 0

for _ in range(n):
    d, r, g = map(int, input().split())
    
    t += d - pre
    pre = d

    red = t % (r+g)
    
    if red <= r:
        t += r - red
    
print(t+(l-pre))