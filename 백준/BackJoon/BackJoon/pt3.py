import sys

input = sys.stdin.readline

def confirm(k):
    count = 0

    if k == 1:
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    count += 1
    else:
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    isTrue = True
                    if i+k < n and j+k < n:
                        for ti in range(i, i+k):
                            if isTrue == False:
                                break
                            for tj in range(j, j+k):
                                if matrix[ti][tj] != 1:
                                    isTrue = False
                                    break

                        if isTrue:
                            count += 1  
                else:
                    continue

    return count

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip())))

total = 0
sizes = {}

for i in range(1,n+1):
    size = confirm(i)
    if size == 0:
        break
    else:
        sizes[i] = confirm(i)

for i in sizes.values():
    total += int(i)

print("total: {}".format(total))

for idx in sizes.keys():
    print("size[{}]: {}".format(idx, sizes[idx]))


