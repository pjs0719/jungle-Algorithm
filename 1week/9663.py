def n_queens(n):
    def is_safe(board, row, col):
        # 같은 열에 다른 퀸이 있는지 확인
        for i in range(row):
            if board[i] == col:
                return False
        
        # 왼쪽 대각선에 다른 퀸이 있는지 확인
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i] == j:
                return False
        
        # 오른쪽 대각선에 다른 퀸이 있는지 확인
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i] == j:
                return False
        
        return True

    def solve(board, row):
        if row == n:  # 모든 행에 퀸을 배치했다면
            solutions.append(board[:])  # 현재 배치를 결과 리스트에 저장
            return
        
        for col in range(n):  # 각 열을 순회하며 가능한 위치 탐색
            if is_safe(board, row, col):  # 현재 위치가 유효하다면
                board[row] = col  # 퀸 배치
                solve(board, row + 1)  # 다음 행으로 이동
                board[row] = -1  # 백트래킹 (퀸 제거)

    solutions = []  # 모든 가능한 배치를 저장할 리스트
    board = [-1] * n  # 각 행의 퀸 위치를 저장 (-1은 비어 있음을 의미)
    solve(board, 0)
    return solutions


# 테스트 실행
n = 4
solutions = n_queens(n)
print(f"N={n}일 때 가능한 해의 개수: {len(solutions)}")
for solution in solutions:
    print(solution)
