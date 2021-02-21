# 조합 순열 공부하기
# https://ourcstory.tistory.com/414

from itertools import permutations

n = int(input())

array = permutations(list(map(int, input().split()))) # 이게 어떻게 나오는 지를 보기
answer = 0

for i in array:
    sums = 0
    for j in range(n-1):
        sums += abs(i[j] - i[j+1])
    answer = max(answer, sums)    

print(answer)