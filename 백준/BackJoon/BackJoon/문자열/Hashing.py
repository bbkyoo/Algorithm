import sys

input = sys.stdin.readline

l = int(input())
s = input().strip('\n')

dic = {}
num = 1
for i in range(97,123):
    dic[chr(i)] = num
    num += 1

result = 0
for i in range(len(s)):
    result += (dic[s[i]])*(31**i)    

print(result % 1234567891)