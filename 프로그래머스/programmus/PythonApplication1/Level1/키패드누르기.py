def solution(numbers, hand):  
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    result = []
    current_l = '*'
    current_r = '#'

    l_x, l_y = 0, 0
    r_x, r_y = 0, 0
    n_x, n_y = 0, 0
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            result.append('L')
            current_l = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            result.append('R')
            current_r = numbers[i]
        else:
            for j in range(len(keypad)):
                for k in range(len(keypad[j])):

                    if keypad[j][k] == current_l:
                        l_x, l_y = j, k

                    elif keypad[j][k] == current_r:
                        r_x, r_y = j, k

                    if keypad[j][k] == numbers[i]:
                        n_x, n_y = j, k

            if abs(n_x - l_x) + abs(n_y - l_y) == abs(n_x - r_x) + abs(n_y - r_y):
                if hand == 'right':
                    result.append('R')
                    current_r = numbers[i] 
                else:
                    result.append('L')
                    current_l = numbers[i]

            elif abs(n_x - l_x) + abs(n_y - l_y) > abs(n_x - r_x) + abs(n_y - r_y):
                result.append('R')
                current_r = numbers[i]
            else:
                result.append('L')
                current_l = numbers[i]

    return ''.join(result)



