A, B, C = map(int, input().split())

def solution(A, B, C):
    if B == 0:
        return 1 % C  # 0^0 방지
    if B == 1:
        return A % C
    
    # B가 짝수일 때
    if B % 2 == 0:
        temp = solution(A, B//2, C)
        return (temp * temp) % C
    # B가 홀수일 때
    else:
        temp = solution(A, B//2, C)
        return (temp * temp * A) % C

print(solution(A, B, C))

걍 모듈러가 이해가 안가네