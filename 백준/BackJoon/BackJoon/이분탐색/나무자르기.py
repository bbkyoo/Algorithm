import sys

def binary(N, wood, start, end):
    while start <= end:
        count = 0
        mid = (start + end) // 2
        for x in wood:
            if x - mid > 0:
                count += (x - mid)
                
        if count >= M:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
        
    return ans

input = sys.stdin.readline

N, M = map(int, input().split())
wood = list(map(int, input().split()))

start = 0
end = max(wood)

result = binary(N, wood, start, end)
print(result)

