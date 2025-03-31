from collections import deque  # BFS 구현을 위해 deque 사용

# 입력 처리: 정점(N), 간선(M), 시작 노드(V)
N, M, V = map(int, input().split())

# 그래프 초기화: 각 노드에 대해 빈 리스트 생성
graph = {i: [] for i in range(1, N + 1)}

# 간선 정보 입력 및 양방향 그래프 구성
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)  # v1에서 v2로 가는 간선 추가
    graph[v2].append(v1)  # v2에서 v1로 가는 간선 추가

# 문제 요구사항: 번호가 작은 노드부터 방문하기 위해 정렬
for node in graph:
    graph[node].sort()


# BFS 함수 정의
def bfs(graph, start, N):
    # 방문 여부를 저장하는 리스트 (0번 인덱스는 사용하지 않음)
    visited = [False] * (N + 1)
    
    # BFS 결과를 저장할 리스트
    result = []
    
    # BFS 탐색에 사용할 큐 초기화 (시작 노드 추가)
    q = deque([start])
    
    # 시작 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 노드를 하나 꺼냄
        current = q.popleft()
        
        # 현재 노드를 결과 리스트에 추가
        result.append(current)
        
        # 현재 노드와 연결된 모든 인접 노드 탐색
        for neighbor in graph[current]:
            # 아직 방문하지 않은 노드만 큐에 추가
            if not visited[neighbor]:
                visited[neighbor] = True  # 방문 처리
                q.append(neighbor)       # 큐에 추가
    
    return result  # BFS 탐색 결과 반환

def dfs(graph, start, N):
    visited = [False] * (N + 1)
    result = []
    stack = [start]  # 리스트로 스택 구현
    
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            # 역순으로 스택에 추가 (중요!)
            for neighbor in reversed(graph[current]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return result

def dfs_recursive(graph, current, visited, result):
    # 현재 노드를 방문 처리
    visited[current] = True
    result.append(current)

    # 현재 노드의 인접 노드 탐색
    for neighbor in graph[current]:
        if not visited[neighbor]:  # 방문하지 않은 노드만 탐색
            dfs_recursive(graph, neighbor, visited, result)  # 재귀 호출



visited = [False] * (N + 1)  # 방문 체크 배열
result = []    
dfs_recursive(graph, V, visited, result)
print(*result)
print(*bfs(graph, V, N))