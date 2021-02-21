M = int(input())

lst = [1,2,3]

for _ in range(M):
    x,y = map(int, input().split())
     
    lst[lst.index(x)], lst[lst.index(y)] = lst[lst.index(y)], lst[lst.index(x)]

print(lst[0])


# 이건 왜 맞음?
#N = int(input())

#cups = [1,2,3]
#for _ in range(N):
#    x, y = map(int, input().split())
    
#    xi = cups.index(x)
#    yi = cups.index(y)
    
#    cups[xi], cups[yi] = cups[yi], cups[xi]
    
#print(cups[0])