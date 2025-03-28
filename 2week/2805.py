N,M = map(int, input().split())
T = list(map(int, input().split()))



max = max(T)
add = 0
low, hi = 0, max


while low <= hi:
    mid = (low + hi) // 2
    add = 0
    for i in T:
        if i >= mid:
            add += i-mid

    if add >= M:  
        result = mid
        low = mid + 1
    else:
        hi = mid - 1

print(result)