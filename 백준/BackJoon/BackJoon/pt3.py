# 문제 1번
# import math
#
# def solution(b):
#     for i in range(1, b+1):
#         if str(math.sqrt(i**2 + b**2))[-2:] == '.0':
#             return int(math.sqrt(i**2 + b**2))
#     return -1
#
# 문제 2번
# s = ''
# s1 = "ppwwwbpbbwwbw"
# s2 = "pwbwpwwbw"
# mn = min(len(s1), len(s2))
#
# if len(s1) > len(s2):
#     st1 = s1
#     st2 = s2
# else:
#     st1 = s2
#     st2 = s1
#
# for i in range(mn):
#     if st2[-1-i] == st1[-1-i]:
#         s += st2[-1-i]
#     elif st2[-1-i] == 'p' and st1[-1-i] == 'b':
#         s += 'p'
#     elif st2[-1 - i] == 'w' and st1[-1 - i] == 'b':
#         s += 'b'
#     elif st2[-1 - i] == 'b' and st1[-1 - i] == 'w':
#         s += 'b'
#     elif st2[-1 - i] == 'b' and st1[-1 - i] == 'p':
#         s += 'b'
#     elif st2[-1 - i] == 'p' and st1[-1 - i] == 'w':
#         s += 'w'
#
# s = list(s)
# s.reverse()
# s = ''.join(s)
# result = ''
# for i in range(len(st1) - len(st2)):
#     result += st1[i]
# result += s
#
# init = 32
# answer = 0
# isP = 0
# cnt = 0
# for i in result:
#     if i == 'p':
#         init //= 2
#         isP += 1
#     elif i == 'w':
#         if isP:
#             cnt += 1
#         if cnt == 4 and isP:
#             cnt = 0
#             init *= 2
#             isP -= 1
#     elif i == 'b':
#         answer += init*init
#         if isP:
#             cnt += 1
#         if cnt == 4 and isP:
#             cnt = 0
#             init *= 2
#             isP -= 1
#
# print(answer)
#
# 문제 3번
# def solution(n):
#     s = []
#     num = 0
#     while n > 0:
#         s.append(n % 2)
#         n //= 2
#     for i in range(len(s)):
#         if s[i] == 1:
#             num += 3 ** i
#     return num