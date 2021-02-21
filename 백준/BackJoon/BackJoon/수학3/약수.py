n = int(input())

num = list(map(int, input().split()))
num_max = max(num)
num_min = min(num)

print( num_max * num_min )