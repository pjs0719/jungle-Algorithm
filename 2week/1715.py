import heapq

heap = []
total = 0

for _ in range(int(input())):
    N = int(input())
    heapq.heappush(heap, N)


while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    total += a + b 


print(total)