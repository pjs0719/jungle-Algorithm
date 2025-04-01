import heapq

# 입력 처리 및 변수 선언
N = int(input())
M = int(input())
city = {i: {} for i in range(1, N+1)}

for _ in range(M):
    a, b, w = map(int, input().split())
    if b in city[a]:  # 중복 간선 처리
        city[a][b] = min(city[a][b], w)
    else:
        city[a][b] = w

start, end = map(int, input().split())

dis = [float('inf')] * (N+1)  # 수정: 문자열 -> 무한대 숫자
dis[start] = 0  # 추가: 시작점 거리 초기화
heap = []
heapq.heappush(heap, (0, start))  # 추가: 시작점 힙에 삽입

def dij():
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        
        # 수정: 방문 배열 대신 거리 비교
        if current_dist > dis[current_node]:
            continue
            
        for neighbor in city[current_node]:
            new_dist = current_dist + city[current_node][neighbor]
            
            # 수정: 리스트 append -> 값 비교 후 갱신
            if new_dist < dis[neighbor]:
                dis[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))  # 추가: 갱신 시 힙에 삽입

dij()
print(dis[end])
