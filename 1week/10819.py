N = int(input())
A_list = list(map(int, input().split()))
ans = []


def solution():
    if ans == N
        ans



solution([])













# 입력 받기
n = int(input())  # 배열의 크기 N 입력
nums = list(map(int, input().split()))  # N개의 정수를 입력받아 리스트로 저장

# 전역 변수 설정
visited = [False] * n  # 각 숫자의 사용 여부를 추적하는 배열 (초기값: 모두 False)
max_total = 0  # 최대 차이 합을 저장할 변수

def backtrack(count, prev, total):
    global max_total  # 전역 변수 max_total을 함수 내에서 수정하기 위한 선언
    
    # 종료 조건: 모든 숫자를 사용했을 때 (순열 완성)
    if count == n:
        max_total = max(max_total, total)  # 현재까지의 최대값과 비교하여 더 큰 값으로 갱신
        return
    
    # 모든 숫자에 대해 반복
    for i in range(n):
        if not visited[i]:  # 아직 사용하지 않은 숫자라면
            visited[i] = True  # 현재 숫자를 사용했다고 표시
            
            # 새로운 차이 계산 및 누적
            # count가 0일 때(첫 번째 숫자 선택 시)는 이전 숫자가 없으므로 차이를 더하지 않음
            new_total = total + abs(nums[i] - prev) if count != 0 else 0
            
            # 재귀 호출: 다음 숫자 선택
            # count + 1: 선택한 숫자 개수 증가
            # nums[i]: 현재 선택한 숫자를 다음 호출의 prev로 전달
            # new_total: 지금까지의 누적 차이 합
            backtrack(count + 1, nums[i], new_total)
            
            visited[i] = False  # 백트래킹: 현재 숫자를 사용하지 않은 상태로 되돌림

# 백트래킹 시작
# 초기 호출: 선택한 숫자 없음(count=0), 이전 숫자 없음(prev=0), 누적 합 없음(total=0)
backtrack(0, 0, 0)

# 최종 결과 출력
print(max_total)
