from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = {i:[] for i in range(1,N+1)}
q = deque()
result = []


for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

for j in range(1, N+1):
    if in_degree[j] == 0:
        q.append(j)

while q:
    a = q.popleft()
    result.append(a)
    k = graph[a]
    for s in k:
        in_degree[s] -= 1
        if in_degree[s] == 0:
            q.append(s)
   
 
print(*result)