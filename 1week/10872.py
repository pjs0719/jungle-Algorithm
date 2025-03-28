N = int(input())


def solution(n): 
    if n == 0:
        return 1
    elif n != 1:
        a = n * solution(n-1)
        return a
    else:
        return 1
    
print(solution(N))
    

# math 이용하기
import math
print(math.perm(int(input())))