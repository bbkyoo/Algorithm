#두 개의 단어가 같은 종류의 문자로 이루어져 있다.
#같은 문자는 같은 개수 만큼 있다.
# 두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다.

import sys

input = sys.stdin.readline

n = int(input())
words = [[0 for _ in range(26)] for _ in range(n)]
for i in range(n):
    string = input().rstrip()
    for s in string:
        words[i][ord(s) - ord('A')] += 1

res = 0
for word in words[1:]:
    plus, minus = 0, 0
    for i in range(26):
        if word[i] > words[0][i]:
            plus += (word[i] - words[0][i])
        else:
            minus += (words[0][i] - word[i])

    if plus < 2 and minus < 2:
        res += 1

print(res)



















