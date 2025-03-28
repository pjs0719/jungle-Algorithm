from collections import deque

N = int(input())  # 보드 크기
K = int(input())  # 사과 개수
board = [[0] * N for _ in range(N)]  # 보드 초기화
for _ in range(K):  # 사과 위치 저장
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1  # (1,1)을 (0,0)으로 변환해서 저장

L = int(input())  # 방향 변환 정보 개수
moves = {}  # 방향 변환 정보를 딕셔너리로 저장
for _ in range(L):
    X, C = input().split()
    moves[int(X)] = C  # {시간: 'L' 또는 'D'}

# 방향 (우, 하, 좌, 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 처음 방향 (오른쪽)

# 뱀 초기 설정
snake = deque([[0, 0]])  # 뱀의 몸 위치 저장
time = 0  # 시간
while True:
    time += 1
    head_x, head_y = snake[-1]  # 현재 머리 위치
    new_x, new_y = head_x + dx[direction], head_y + dy[direction]  # 새로운 머리 위치

    # 벽 충돌 or 자기 몸 충돌 체크
    if not (0 <= new_x < N and 0 <= new_y < N) or [new_x, new_y] in snake:
        break  # 게임 종료

    # 이동 처리
    snake.append([new_x, new_y])  # 새로운 머리 추가
    if board[new_x][new_y] == 1:  # 사과 먹으면 꼬리 유지
        board[new_x][new_y] = 0  # 사과 제거
    else:
        snake.popleft()  # 사과 없으면 꼬리 줄이기

    # 방향 전환
    if time in moves:
        if moves[time] == 'L':  # 왼쪽 회전
            direction = (direction - 1) % 4
        else:  # 오른쪽 회전
            direction = (direction + 1) % 4

print(time)  # 게임이 끝나는 시간 출력
