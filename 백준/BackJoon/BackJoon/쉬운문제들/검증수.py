a,b,c,d,e = map(int, input().split())
result = ((a*a) + (b*b) + (c*c) + (d*d) + (e*e)) % 10
print(result)