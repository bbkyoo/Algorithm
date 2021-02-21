piece = list(map(int, input().split()))

result = sorted(piece)

def solve(piece):
    for i in range(1,5):
        if piece[i-1] > piece[i]:
            piece[i-1], piece[i] = piece[i], piece[i-1]
            for j in range(5):
                print(piece[j], end=" ")
            print()
 
while result != piece:
    solve(piece)




 
