N = int(input())

def solution(n):
    if n < 2:
        return 1
    
    return solution(n-1) * n

print(solution(N))