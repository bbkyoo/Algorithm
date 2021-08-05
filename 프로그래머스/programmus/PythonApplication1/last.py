def solution(n, lost, reserve):
    student = [i for i in range(1, n+1)]

    lost.sort()
    reserve.sort()
    temp = []

    for i in range(len(reserve)):
         if reserve[i] in lost:
             temp.append(i)
             lost.pop(lost.index(reserve[i]))

    while temp:
        reserve.pop(temp[-1])
        temp.pop(-1)

