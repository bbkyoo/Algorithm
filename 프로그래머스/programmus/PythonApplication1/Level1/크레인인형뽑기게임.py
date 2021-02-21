# 격자의 상태가 담긴 2차원 배열 board
# 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요

def solution(board, moves):
    answer = 0
    box = [0]
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                box.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                
                if box[-1] == box[-2]:
                    box = box[:-2]
                    answer += 2
                break    
                
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
