S = input()
P = input()

i = 0
cnt = 0
while i < len(P):
    temp = 0
    for j in range(len(P), 0, -1):
        if P[i:j] in S:
            temp = j - i
            break

    if temp != 0:
        i += temp
        cnt += 1
    else:
        i += 1

print(cnt)