# https://johnyejin.tistory.com/127

def rotation(arr):
    n = len(arr)
    ret = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]

    return ret

def check(startX, startY, key, lock, expendSize, start, end):
    expendList = [[0]*expendSize for _ in range(expendSize) ]

    for i in range(len(key)):
        for j in range(len(key)):
            expendList[startX + i][startY + j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            expendList[i][j] += lock[i-start][j-start]
            if expendList[i][j] != 1:
                return False
    return True

def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    expendSize = len(lock) + start * 2

    for a in range(0, 4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expendSize, start, end):
                    return True
        key = rotation(key)
    return False







