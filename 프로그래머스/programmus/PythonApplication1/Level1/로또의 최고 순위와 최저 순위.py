def solution(lottos, win_nums):
    lottos.sort(reverse=True) 
    win_nums.sort(reverse=True)

    mx = 6
    mn = 6
    temp = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            temp += 1
            if temp >= 2:
                mx -= 1
        elif lottos[i] in win_nums:
            temp += 1
            if temp >= 2:
                mx -= 1
                mn -= 1
    answer = [mx,mn]
    return answer