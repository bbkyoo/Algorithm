#def solution(arr):
#    answer = []
#    return answer

# 최종적으로 남는 0의 개수와 1의 개수


def solution(arr):
    x = 0
    y = 0
    check = arr[x][y]

    for i in range(x, x+len(arr)):
        for j in range(y, y+len(arr)):
            if check != arr[i][j]:
                solution(x,y,n//2)
                solution(x,y,n//2)
                solution(x,y,n//2)
                solution(x,y,n//2)
            