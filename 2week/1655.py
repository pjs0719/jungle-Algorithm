import heapq
import sys

input = sys.stdin.readline  # 빠른 입력을 위해 사용

maxheap = []  # 중간값 이하의 값들 (최대 힙, 음수로 저장)
minheap = []  # 중간값 이상의 값들 (최소 힙, 기본 저장)

n = int(input())

for _ in range(n):
    num = int(input())

    # 1. 최대 힙과 최소 힙에 적절하게 삽입
    if not maxheap or num <= -maxheap[0]:  
        heapq.heappush(maxheap, -num)  # 최대 힙 (음수 저장)
    else:
        heapq.heappush(minheap, num)  # 최소 힙 (그대로 저장)

    # 2. 힙 균형 조정 (maxheap이 minheap보다 많거나 같아야 함)
    if len(maxheap) > len(minheap) + 1:
        heapq.heappush(minheap, -heapq.heappop(maxheap))
    elif len(maxheap) < len(minheap):
        heapq.heappush(maxheap, -heapq.heappop(minheap))

    # 3. 중앙값 출력 (maxheap[0]이 항상 중앙값)
    print(-maxheap[0])












#x번지의 왼쪽.오른쪽 2x,2x+1
#x번지의 부모 x/2











# mid = []
# for _ in range(int(input())):
#     num = int(input())
#     # 효율적인 삽입
#     import bisect
#     bisect.insort(mid, num)
    
#     n = len(mid)
#     if n % 2 == 0:
#         # 짝수 길이: 두 중간값 중 작은 값
#         print(mid[n//2 - 1])
#     else:
#         # 홀수 길이: 중앙값
#         print(mid[n//2])
