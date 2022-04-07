s = input()
temp = ''
temp += s[0]
for i in range(1, len(s)):
    if temp[0] >= s[i]:
        temp = temp[::-1]
        temp += s[i]
        temp = temp[::-1]
    else:
        temp += s[i]

print(temp)