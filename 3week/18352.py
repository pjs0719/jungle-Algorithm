from collections import deque
N, M, K, X = map(int, input().split())
city = {i: [] for i in range(1, N + 1)}
count = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    city[a].append(b)

def bfs(city, X):
    d = deque([(X, 0)])
    count[X] = 0

    while d:
        current, dist = d.popleft()
        for next_city in city[current]:
            if count[next_city] == -1:  # 방문하지 않은 도시만 추가
                count[next_city] = dist + 1
                d.append((next_city, dist + 1))


bfs(city, X)
result = []

for i in range(len(count)):
    if count[i] == K:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print("-1")
