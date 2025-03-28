def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    a = n // 2  # 중앙값에서 시작
    b = n - a   # a + b = n 유지
    
    # a를 1씩 줄이며 두 수가 모두 소수인지 확인
    while a > 1:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b = n - a  # b는 자동으로 n - a

# 일단 스킵. 1시간 초과

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

MAX = 10000
is_prime = sieve_of_eratosthenes(MAX)

T = int(input())
for _ in range(T):
    n = int(input())
    for a in range(n//2, 1, -1):
        if is_prime[a] and is_prime[n-a]:
            print(a, n-a)
            break



# #💡 핵심 힌트
# 소수 리스트 미리 준비: 10,000까지의 모든 소수를 미리 구해놓고 시작하세요 (에라토스테네스의 체 활용).
# 중심에서 시작: 주어진 짝수를 반으로 나눈 값부터 시작해, 하나씩 줄여가며 두 수가 모두 소수인지 확인하세요.
# 🔍 생각의 흐름
# 소수 판별 최적화: 큰 범위의 소수를 반복적으로 판별해야 하므로, 미리 체로 걸러둡니다.
# 차이 최소화 전략: 두 소수의 차이가 가장 작은 경우는 중앙값에서 가장 가까운 쌍일 확률이 높습니다.
# 탐색 방향: 중앙값에서 점점 멀어지며 탐색하면 첫 번째 발견된 쌍이 차이가 가장 작습니다.
# 실마리 예시
# 짝수 n=16을 예로 들면:
# 중앙값 8부터 시작 → 8(소수 아님)
# 다음 후보 7과 9 → 9(소수 아님)
# 다음 후보 5와 11 → 둘 다 소수!
# → 5 + 11이 정답!