from collections import deque

N = int(input())

d = deque(range(1, N+1))


while len(d) > 1:
    d.popleft()
    d.rotate(-1)

print(d[0])