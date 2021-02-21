text = input()
bomb = input()

ans = []

for i in text:
    ans.append(i)
    if len(ans) >= len(bomb):
        check = []
        checkcount = 0
        same = True
        for j in range(-1,(-len(bomb))-1,-1):
            if ans[j] != bomb[j]:
                same = False
                break

        if same == True:
            a = 0
            while a < len(bomb):
                ans.pop()
                a += 1

if len(ans) == 0:
    print("FRULA")
else:
    str = ""
    for i in ans:
        str += i
    print(str)