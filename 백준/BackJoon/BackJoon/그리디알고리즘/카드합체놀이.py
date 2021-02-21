import sys

input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

while m:
    card.sort()
    temp = card[0] + card[1]
    card[0] = temp
    card[1] = temp
    
    m -= 1

print(sum(card))