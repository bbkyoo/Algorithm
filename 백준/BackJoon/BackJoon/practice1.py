n = int(input())

hours = []
for _ in range(n):
    hour = input().split("~")
    hours.append(hour)

front = max(hours,key = lambda x : x[0])[0]
back = min(hours,key = lambda x : x[1])[1]

f_h = 0
f_m = 0
b_h = 0
b_m = 0

f_h = int(front[:front.index(':')])
f_m = int(front[front.index(':')+1:])
b_h = int(back[:back.index(':')])
b_m = int(back[back.index(':')+1:])

if f_h > b_h:
    print(-1)
elif f_h == b_h and f_m > b_m:
    print(-1)
else:
    print(front + '~' + back)



    