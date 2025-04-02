import heapq

n = int(input())
miro = [list(map(int, input().strip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = 0  # 시작점 (0,0)
    
    heap = []
    heapq.heappush(heap, (0, 0, 0))  # (비용, x, y)
    
    while heap:
        current_cost, x, y = heapq.heappop(heap)
        
        if x == n-1 and y == n-1:  # 도착지
            return current_cost
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                # 다음 칸이 흰 방이면 cost 0, 검은 방이면 cost 1
                cost = 0 if miro[nx][ny] == 1 else 1
                new_cost = current_cost + cost
                
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))
    
    return dist[n-1][n-1]

print(dijkstra())
