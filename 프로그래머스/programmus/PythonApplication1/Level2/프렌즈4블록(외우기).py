# https://wikidocs.net/16044

def pop_num(matrix, m, n):
    pop_set = set()

    # search
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == matrix[i-1][j-1] == matrix[i-1][j] == matrix[i][j-1] != '_':
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)]) # | - 합집합 연산자, a |= b는 => a는 a와b의 합집합 형태, b는 그대로 이다.  

    # set_board
    for i, j in pop_set:
        matrix[i][j] = 0

    for i, row in enumerate(matrix):
        empty = ['_'] * row.count(0)
        matrix[i] = empty + [block for block in row if block != 0]
        
    return len(pop_set)

                
def solution(m, n, board):
    count = 0
    matrix = list(map(list,zip(*board))) # board 행을 열로 바꾸는 코드

    while True:
        pop = pop_num(matrix, m, n)
        if pop == 0:
            return count
        count += pop













