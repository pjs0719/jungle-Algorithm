from collections import deque

     #상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

miro = []
bfs_q = deque()

n,m = map(int, input().split())
for _ in range(n):
    miro.append(list(map(int, input())))


def bfs(miro):
    bfs_q.append((0, 0))

    while bfs_q:
        x, y = bfs_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1  # 이동한 칸의 거리 업데이트
                bfs_q.append((nx, ny))  # 새로운 좌표 추가

    print(miro[n-1][m-1])

bfs(miro)