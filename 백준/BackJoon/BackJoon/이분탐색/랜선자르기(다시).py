#랜선의 길이를 움직여 랜선 개수를 채우는지 보는 것이다.

#1) 가장 짧은 길이 1을 start로, 랜선 중 가장 긴 길이를 end로 둔다.
#2) 이분탐색이 끝날 때까지 while 문을 돌린다.
#3) mid를 start와 end의 중간으로 두고, 모든 랜선 값을 mid로 나누어 총 몇개의 랜선이 나오나 살펴본다.
#4-1) 랜선이 목표치 이상이면 mid+1을 start로 두고 다시 while문 반복
#4-2) 랜선이 목표치 이하면 mid-1을 end로 두고 다시 while문 반복
#5) start와 end가 같아지면: 조건을 만족하는 최대의 랜선길이를 찾으면 탈출한다.
#6) 결과값인 end출력

import sys

def binary(N, li ,start, end):
    while start <= end:
        mid = (end + start) //2 
        count = sum([x//mid for x in li])
        if count < N:
            end = mid - 1
        elif count >= N:
            start = mid + 1
            ans = mid
    return ans
input = sys.stdin.readline

K, N = map(int, input().split())
li = []

for _ in range(K):
    li.append(int(input()))
 
end, start = max(li), 1

ans = binary(N, li, start, end)

print(ans)

