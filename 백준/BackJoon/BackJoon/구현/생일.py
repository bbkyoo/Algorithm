import sys

input = sys.stdin.readline

n = int(input())

birthday = []

for _ in range(n):
    name, day, month, year = map(str, input().split())
    birthday.append([name, int(day), int(month), int(year)])

birthday.sort(key = lambda x: (-x[3],-x[2],-x[1]))

print(birthday[0][0])
print(birthday[-1][0])