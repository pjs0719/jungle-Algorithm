
N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
visit = [False]*(N+1)
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(s):
    visit[s] = True
    for neighbor in graph[s]:
        if not visit[neighbor]:
            dfs(neighbor)
    return visit

for i in graph:
    if not visit[i]:
        count += 1
        dfs(i)
        

print(count)