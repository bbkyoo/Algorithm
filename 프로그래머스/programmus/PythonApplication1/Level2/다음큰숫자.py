def twice(n):
    lt = []

    while n != 1:
        lt.append(n%2)
        n //= 2
    lt.append(n)
    lt.reverse()
    return lt

def solution(n):
    k = n+1
    lt = twice(n)
    count_ori = 0
    for i in lt:
        if i == 1:
            count_ori += 1

    count_sam = 0
    while count_ori != count_sam:
        count_sam = 0
        temp = twice(k)
        for i in temp:
            if i == 1:
                count_sam +=1

        k += 1

    return (k-1)


