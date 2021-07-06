s = input()

temp = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        temp.append(s[i:j])

print(len(set(temp)))
