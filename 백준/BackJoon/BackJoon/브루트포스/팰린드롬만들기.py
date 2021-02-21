def isPellindrom(s): 
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True

s = input()

if isPellindrom(s):
    print(len(s))
else:
    for i in range(1, len(s)+1):
        temp = s
        for j in range(i):
            temp += s[i-j-1]    

        if isPellindrom(temp):
            print(len(temp))
            break




