# https://velog.io/@good159897/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-%EB%89%B4%EC%8A%A4-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81 보기

#def solution(str1, str2):
#    answer = 0
#    return answer

str1 = "E=M*C^2"
str2 = "AAAA12"
str1 = str1.upper()
str2 = str2.upper()

s1 = []
s2 = []

for i in str1:
    if i.isalpha():
        s1.append(i)

for i in str2:
    if i.isalpha():
        s2.append(i)

temp_s1 = []
temp_s2 = []

for i in range(1, len(s1)):
    temp_s1.append(s1[i-1] + s1[i])

for i in range(1, len(s2)):
    temp_s2.append(s2[i-1] + s2[i])


s_entile = []
s_collect = []

for i in range(len(temp_s1)):
    if temp_s1[i] not in s_entile:
        s_entile.append(temp_s1[i])
        
for i in range(len(temp_s2)):
    if temp_s2[i] not in s_entile:
        s_entile.append(temp_s2[i])
    elif temp_s2[i] in s_entile:
        s_collect.append(temp_s2[i])

result = 0
if len(s_entile) == len(s_collect):
    result = 1
else:
    result = len(s_collect) / len(s_entile)

print(round(result * 65536))







