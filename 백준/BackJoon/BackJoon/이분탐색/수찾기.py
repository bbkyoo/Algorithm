import sys

input = sys.stdin.readline

N = int(input())
n_card = list(map(int, input().split()))
n_card.sort()

M = int(input())
m_card = list(map(int, input().split()))

def binary(n, n_card, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if n == n_card[m]:
        return n_card[start:end+1].count(n)
    elif n < n_card[m]:
        return binary(n, n_card, start, m-1)
    else:
        return binary(n, n_card, m+1, end) 

n_dic = {}

for n in n_card:
    start = 0
    end = len(n_card) -1
    if n not in n_dic:
        n_dic[n] = binary(n, n_card, start, end)

for i in m_card:
    if i in n_dic:
        print('1')
    else:
        print('0')

