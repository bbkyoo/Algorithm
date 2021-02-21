A, B, V = map(int, input().split())
day = 0

if (V-B)%(A-B) != 0:
    day = (V-B)//(A-B) + 1
else:
    day = (V-B)//(A-B)
   
print(day)

