x = input()

count = 0
while len(x) != 1:
    temp = 0
    for i in x:
        temp += int(i)
    x = str(temp)
    count += 1

result = ''
if int(x) % 3 == 0:
    result = "YES"
else:
    result = "NO"

print(count)
print(result)