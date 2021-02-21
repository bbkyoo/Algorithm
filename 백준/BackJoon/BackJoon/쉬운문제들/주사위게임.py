N = int(input())

num = []
for i in range(N):
    a ,b, c = map(int, input().split())
    if a == b and b == c:
        num.append(10000+ (a*1000))
    elif (a == b and b != c):
        num.append(1000 + (a*100))
    elif (b == c and c != a):
        num.append(1000 + (b*100))
    elif (c == a and a != b):
        num.append(1000 + (c*100))
    else:
        num.append(max(a,b,c)*100)

print(max(num))