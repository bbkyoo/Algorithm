# 이 문제는 아래에서 부터 생각을 해야한다.
# 마지막 행에 모든 합들을 구하고 거기에서 최댓값을 찾는 것 이다.
# 맨 왼쪽과 맨 오른쪽은 바로 위를 가르킨다
# 그 이외에는 위의 둘 중 큰 수를 찾아서 간다.

n = int(input())
sum = 0

tri = [] 
for i in range(n):
    tri.append(list(map(int,input().split())))

k = 2
for i in range(1,n):
    for j in range(k):
        if j == 0:
            tri[i][j] = tri[i][j] + tri[i-1][j]
        elif j == i:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            tri[i][j] = tri[i][j] + max(tri[i-1][j], tri[i-1][j-1])
    k += 1

# print(max(tri[n-1]))
print(tri)


        