import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr))) # 정렬 후

dic = {arr2[i] : i for i in range(len(arr2))} # { dict[요소] : 요소의 index }
for i in arr:
    print(dic[i], end=" ")