import sys

input = sys.stdin.readline

n = int(input())

water = list(map(int, input().split()))
water.sort()

start = 0
end = n-1

result = abs(water[start] + water[end]) 
part1 = 0
part2 = 0

while start != end:
    sum = water[start] + water[end]
    
    if abs(sum) <= result:
        result = abs(sum)
        part1 = water[start]
        part2 = water[end]

    if sum > 0:
        end -= 1
    elif sum <= 0:
        start += 1

print(part1, part2)    