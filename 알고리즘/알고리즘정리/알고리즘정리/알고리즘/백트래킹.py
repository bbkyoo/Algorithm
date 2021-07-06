# 1. 백 트래킹
# - 이건 알고리즘 보단 문제해결 하는 전략임
# - 해를 찾기 위해, 후보군에서 제약 조건을 점진적으로 체크하다가 backtrack(다시는 이 후보군
#   을 체크하지 않을 것을 표기)하고, 바로 다른 후보군을 넘어가며 결국 최적의 해를 찾는 방법
# - 모든 경우의 수(후보군)를 상태공간트리를 통해 포현
# - 후보군을 DFS방식으로 확인

# 2. N Queen 문제 코드작성

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row]-current_col) == current_row - queen_row:
            return False
    return True

def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)
            current_candidate.pop()

def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

print(solve_n_queens(4))






