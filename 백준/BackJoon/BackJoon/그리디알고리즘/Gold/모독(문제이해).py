 # 모든 국회의원을 모독해서 각각의 명예 점수를 1씩 감소시킨다.
 # (1)로 인해 1명이라도 국회의원에서 박탈당한 사람이 발생했다면 국민들의 분노를 이용해 (1)로 돌아간다.
 # (1)에 의해 국회의원에서 박탈당한 사람이 없다면 프로젝트를 종료한다.

import sys

input = sys.stdin.readline

n = int(input())
honor = []

for _ in range(n):
    honor.append(int(input()))

max_honor = 1
action = 0

for num in sorted(honor):
    if num >= max_honor:
        action += num - max_honor
        max_honor += 1

print(action)



























