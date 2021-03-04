# 시간초과 코드
#import sys

#input = sys.stdin.readline

#s = input().rstrip()

#while True:   
#    if len(s) > 4:
#        if "PPAP" in s[1:]:
#            s = s.replace("PPAP","P")
#        else:
#            break
#    elif len(s) == 4:
#        if s == "PPAP":
#            s = "P"
#        else:
#            break
#    else:
#        break
        
#if s == 'P':
#    print("PPAP")
#else:
#    print("NP")

import sys

s = input()

cnt = 0
i = 0
while i < len(s):
    if s[i] == 'P':
        cnt += 1
        i += 1
        continue
    
    if i+1 < len(s):
        if cnt >= 2 and s[i+1] == 'P':
            cnt -= 1
            i += 1
        else:
            print("NP")
            sys.exit()
            break
    else:
        print("NP")
        sys.exit()
        break

    i += 1
            
if cnt == 1:
    print("PPAP")
else:
    print("NP")


    




































