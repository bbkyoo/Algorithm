st = input().upper()
cnt = []

for i in set(st):
    cnt.append(st.count(i))

idx = [i for i,x in enumerate(cnt) if x == max(cnt)] # 이렇게 쓰는게 키포인트

if len(idx) > 1:
    print('?')
else:
    print(list(set(st))[cnt.index(max(cnt))]) #이것도 이해하기







