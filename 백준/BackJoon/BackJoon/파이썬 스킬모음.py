n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_type = ['U','D','L','R']

data = list(map(str, input().split()))
x = 1
y = 1

for i in range(len(data)):
    for j in range(len(move_type)):
        if data[i] == move_type[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    if 0 <= nx < n and 0 <= ny < n:
        x = nx
        y = ny

print(x, y)




for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        temp.append(s[i:j])









s.sort(key = lambda x: (len(x[0]),x[1],x[0]))




