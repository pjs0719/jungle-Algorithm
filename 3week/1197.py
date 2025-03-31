import heapq
v, e = map(int, input().split())
graph = {i: [] for i in range(1, v + 1)}

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w)) 


def prim(graph):
    if not graph:  # 그래프가 비어있는 경우
        return []
    
    # 1. 초기화 단계
    start_node = next(iter(graph))  # 임의의 시작 정점 선택(첫 번째 노드)
    visited = set([start_node])     # 방문한 정점 집합 초기화
    mst = []                        # 최소 신장 트리 저장 리스트
    edge_heap = []                  # (가중치, 현재정점, 다음정점) 저장 힙

    # 2. 시작 정점의 모든 간선을 힙에 추가
    for neighbor, weight in graph[start_node]:
        heapq.heappush(edge_heap, (weight, start_node, neighbor))

    # 3. MST 구성 과정
    while edge_heap:
        weight, current, next_node = heapq.heappop(edge_heap)

        if next_node not in visited:
            visited.add(next_node)
            mst.append((weight))  # 간선 정보 저장

            # 4. 새로 추가된 정점의 인접 간선 탐색
            for neighbor, neighbor_weight in graph[next_node]:
                if neighbor not in visited:
                    heapq.heappush(edge_heap, (neighbor_weight, next_node, neighbor))

    
    
    return sum(mst)

print(prim(graph))

