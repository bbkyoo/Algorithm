# 그러면 해결 방법은 가장 큰 값을 가운데에 놓고 왼쪽 오른쪽 번갈아 가면서 놓으면 된다. 
# 인덱스 차이가 1이나면 통나무들의 높이 차이가 커지므로 인덱스 차이를 2로 두는 곳이 가장 좋다
# 예를 들어 통나무 5개가 있을때 통나무의 크기 순을 1,2,3,4,5 번으로 정렬하면
# 4 2 1 3 5 이렇게 순서가 됐을 때 가장 적은 차를 구할 수 있다.
# 4 와 2는 인덱스 2차이, 1과 3도 2차이, 3과 5도 2차이로 가장 적은 인덱스 차를 구하는 것 

T = int(input())

for _ in range(T):
    N = int(input())
    wood = list(map(int, input().split()))
    
    wood.sort()

    result = 0
    for i in range(2,N):
        c = wood[i] - wood[i - 2]
        result = max(c, result)

    print(result)