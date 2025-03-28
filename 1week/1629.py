
def pow_mod(a, b, m):
    # 재귀 종료 조건: 지수(b)가 1이면 a^1 % m 계산
    if b == 1:
        return a % m
    
    # 분할 정복: 지수를 절반으로 분할하여 재귀 호출
    val = pow_mod(a, b // 2, m)  # a^(b//2) % m 계산
    
    # 합치기: (a^(b//2))^2 = a^b 계산 (모듈러 연산 적용)
    val = (val * val) % m
    
    # 지수가 홀수인 경우 추가로 a를 곱해 보정
    if b % 2 == 0:
        return val  # 짝수인 경우 그대로 반환
    else:
        return (val * a) % m  # 홀수인 경우 a 한 번 더 곱함

# 메인 실행 블록 (스크립트 직접 실행 시 동작)
if __name__ == "__main__":
    # 사용자 입력 받기
    a = int(input("밑 (a): "))        # 거듭제곱의 밑 입력
    b = int(input("지수 (b): "))      # 거듭제곱의 지수 입력
    m = int(input("모듈러스 (m): "))  # 모듈러 값 입력
    
    # 결과 계산 및 출력
    print(f"({a}^{b}) % {m} = {pow_mod(a, b, m)}")
