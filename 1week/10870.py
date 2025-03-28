N = int(input())

def solution(n):
    if n < 2:
        return 1
    
    return solution(n-1) + solution(n-2)

if N==0:
    print("0")
else:
    print(solution(N-1))