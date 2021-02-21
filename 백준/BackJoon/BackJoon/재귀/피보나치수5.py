def pivonachi(num):
    if num <= 1:
        return num
    else:
        return pivonachi(num -1) + pivonachi(num -2)     

N = int(input())
print(pivonachi(N))