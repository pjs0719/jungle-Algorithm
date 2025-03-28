from collections import deque

N, K = map(int,input().split())

d = deque(range(1, N+1))
ans = []

while len(d) >= 1:
    d.rotate(-K)
    ans.append(d.pop())


print(f"<{', '.join(map(str, ans))}>")
