N,M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))

T.sort()


add = []
low, hi = 1, T[-1] - T[0]

while low <= hi:
    mid = (low + hi) // 2
    count = 1 
    last = T[0]


    for i in range(1, N):
        if (T[i] - last) >= mid:
            count +=1
            last = T[i]
    
    if count >= M:  
        result = mid
        low = mid + 1
    else:
        hi = mid - 1

print(result)


