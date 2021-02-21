# meet in the Middle 알고리즘을 사용

n, c = map(int, input().split())
bag = list(map(int, input().split()))

ans = 0
asize = 0
bsize = 0
aSum = []
bSum = []

def calcLeft(i, sum):
    global ans, asize, aSum

    if sum > c:
        return
    if i == n//2:
        aSum.insert(asize, sum)
        asize += 1
        return
    calcLeft(i+1, sum + bag[i])
    calcLeft(i+1, sum)

def calcRight(i, sum):
    global ans, bsize, bSum

    if sum > c:
        return
    if i == n//2:
        bSum.insert(bsize, sum)
        bsize += 1
        return
    calcRight(i+1, sum + bag[i])
    calcRight(i+1, sum)

def binarySearch(start, end, val):
    if start > end:
        return
    mid = (start + end) // 2
    
    if bSum[mid] + val <= c:
        idx = mid
        binarySearch(mid + 1, end, val)
    else:
        return binarySearch(start, mid - 1, val) 

calcLeft(0,0)
calcRight(n//2, 0)

for i in range(bsize):
    for j in range(i+1,bsize):
        if bSum[i] < bSum[j]:
            temp = bSum[i]
            bSum[i] = bSum[j]
            bSum[j] = temp

for i in range(asize):
    idx = -1
    binarySearch(0, bsize-1, aSum[i])
    ans += (idx+1)

print(ans)


































