
N = int(input())
a = 0


def solution(n ,x, y):
    
    if(n > 1):
        solution(n-1, x, 6-x-y)
    
    print(x,y)
    
    if(n > 1):
        solution(n-1, 6-x-y, y)



print((2**N) - 1)

if N <= 20:  # 20 초과 시 경로 출력 생략
    solution(N, 1, 3)

print(a)



