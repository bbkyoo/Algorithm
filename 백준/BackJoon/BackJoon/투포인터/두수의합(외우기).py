# 투포인터 활용한 알고리즘 설명
# 1. 시작점(start)와 끝점(end)이 첫 번째 원소의 인덱스(0)을 가리키도록 한다.
# 2. 현재 부분 합이 M과 같다면, 카운트한다
# 3. 현재 부분 합이 M보다 작거나 같다면, end를 1증가시킨다.
# 4. 현재 부분 합이 M보다 크다면, Start를 1증가시킨다.
# 5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.

# 현재 문제를 풀기위한 방법
# 1. start를 맨 앞에, end를 맨 뒤에 위치
# 2. start + end > x, start + end <= x 두 가지 경우로 나뉜다.
# 3. start + end > x => 합이 x에 가까워지기 위해서는 값이 더 작아져야한다. 즉, end를 왼쪽으로 옮긴다.
# 4. start + end <= x -> 같은 이유로 start를 오른쪽으로 옮긴다.

import sys

input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
x = int(input())
number.sort()

start = 0
end = n-1
count = 0

while start != end:
    sum = number[start] + number[end]
    if sum == x:
        count += 1
        start += 1
    elif sum > x:
        end -= 1
    else:
        start += 1

print(count)