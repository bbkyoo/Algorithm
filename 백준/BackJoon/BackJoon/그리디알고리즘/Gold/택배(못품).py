import sys

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

box = []

for i in range(m):
    s, r, b = map(int, input().split())
    box.append([s,r,b])

box.sort()

result = 0
idx = 0
for i in range(m):
    if box[i][2] <= c:
        c -= box[i][2]
        result += box[i][2]
    else:
        box[i][2] = c
        result += c
        c = 0
        idx = i
        break
        
for i in range(idx):
    for j in range(idx, m):
        if box[i][1] == box[j][0] and box[i][2]:
            if box[i][2] <= box[j][2]:
                result += box[i][2]
                box[i][2] -= box[i][2]
            else:
                result += box[j][2]
                box[i][2] -= box[j][2]
                continue
        elif  
            

print(result)