s = input()

number = ['0','1','2','3','4','5','6','7','8','9']
num = []
alhpa = []
for i in range(len(s)):
    if s[i] in number:
        num.append(s[i])
    else:
        alhpa.append(s[i])

alhpa.sort()

sum = 0
for i in range(len(num)):
    sum += int(num[i])
        
result = ''
for i in alhpa:
    result += i

print(result+str(sum))
