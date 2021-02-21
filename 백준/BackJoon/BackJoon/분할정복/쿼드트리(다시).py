N = int(input())

qt = [list(map(int,input())) for _ in range(N)] # 이러면 이중으로 아주 잘 나뉜다.

def cut(x,y,n):
    # n = 1, 하나의 픽셀만 볼 경우
    if n == 1:
        return str(qt[x][y])

    check = qt[x][y]
    result = []

    for i in range(x, x+n):
        for j in range(y, y+n):
            # 색이 다르면, 다시 분할
            if check != qt[i][j]:
                # append와 extend의 차이는
                # extend는 list, tuple, dict 등의 iterable object를
                # python list의 끝에 append 해주는 것.
                result.append('(')
                result.extend(cut(x,y,n//2))
                result.extend(cut(x,y+n//2,n//2))
                result.extend(cut(x+n//2,y,n//2))
                result.extend(cut(x+n//2,y+n//2,n//2))
                result.append(')')
                return result

    return str(qt[x][y])
    
print(''.join(cut(0,0,N)))
