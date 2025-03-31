n = int(input())
e = int(input())
graph = {i: [] for i in range(1, n+1)}
visit = [False]*(n+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 추가

def dfs(s):
    visit[s] = True
    count = 0
    for neighbor in graph[s]:
        if not visit[neighbor]:
            count += 1 + dfs(neighbor)
    return count

result = dfs(1)
print(result)
