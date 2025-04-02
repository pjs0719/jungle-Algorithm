import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read
data = input().split("\n")

N = int(data[0])  
inout = list(data[1].strip())

# 실내('1') 노드의 집합
indices = {i + 1 for i, l in enumerate(inout) if l == '1'}

walk = {i: [] for i in range(1, N + 1)}

for i in range(2, N + 1):
    a, b = map(int, data[i].split())
    walk[a].append(b)
    walk[b].append(a)

ans = 0

# 1. 실내('1')끼리 직접 연결된 경우 먼저 카운트
for node in indices:
    for neighbor in walk[node]:
        if neighbor in indices:
            ans += 1  # (중복 카운트 방지를 위해 나중에 //2 처리)

# 2. 실외('0')을 중심으로 DFS 탐색하여 연결된 실내('1') 그룹 찾기
visited = [False] * (N + 1)

def dfs(node):
    stack = [node]
    indoor_count = 0  # 연결된 실내('1') 개수

    while stack:
        curr = stack.pop()
        for neighbor in walk[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if neighbor in indices:
                    indoor_count += 1
                else:
                    stack.append(neighbor)

    return indoor_count

for node in range(1, N + 1):
    if inout[node - 1] == '0' and not visited[node]:  # 실외('0') 노드 기준으로 탐색
        visited[node] = True
        count = dfs(node)
        if count >= 2:
            ans += (count * (count - 1)) // 2  # (조합 계산)

# 실내-실내 직접 연결 카운트 나누기 2 (중복 제거)
print(ans // 2)
