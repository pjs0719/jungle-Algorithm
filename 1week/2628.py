def solution(n):
    n.sort()
    max = 0
    for i in range(len(n)-1):
        if max < n[i+1] - n[i]:
            max = n[i+1] - n[i] 
    return max

x, y =map(int, input().split())

x_arr = [0,x]
y_arr = [0,y]

for _ in range(int(input())):
    xy, b = map(int, input().split())
    if xy == 0:
        y_arr.append(b)
    else:
        x_arr.append(b)

x_max = solution(x_arr)
y_max = solution(y_arr)

print(x_max*y_max)
