import sys

input = sys.stdin.readline

def binary(i, card_n, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if i == card_n[mid]:
        return card_n[start:end+1].count(i)
    elif i < card_n[mid]:
        return binary(i, card_n, start, mid-1)
    else:
        return binary(i, card_n, mid+1, end)


n = int(input())
card_n = list(map(int, input().split()))
card_n.sort()

m = int(input())
card_m = list(map(int, input().split()))

n_dic = {}    

for i in card_n:
    start = 0
    end = len(card_n) - 1
    if i not in n_dic:
        n_dic[i] = binary(i, card_n, start, end)

for i in card_m:
    if i in n_dic:
        print(n_dic[i], end=" ")
    else:
        print(0, end=" ")
