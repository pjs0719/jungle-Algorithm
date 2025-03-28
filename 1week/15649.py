N, M = map(int, input().split())

def solution():
































"""

# 입력 받기
N, M = map(int, input().split())
visited = [False] * (N + 1)  # 숫자 방문 여부 추적
result = []  # 현재 순열을 저장할 리스트

def backtrack():
    # 종료 조건: 현재 순열의 길이가 M이면 출력
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    
    # 1부터 N까지 숫자 순회
    for i in range(1, N + 1):
        if not visited[i]:  # 아직 방문하지 않은 숫자라면
            visited[i] = True
            result.append(i)  # 숫자 추가
            backtrack()  # 재귀 호출
            result.pop()  # 선택 취소 (상태 복원)
            visited[i] = False

backtrack()

---
# 입력 받기
N, M = map(int, input().split())
result = []  # 현재 조합을 저장할 리스트

def backtrack(start):
    # 종료 조건: 현재 조합의 길이가 M이면 출력
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    
    # start부터 N까지 숫자 순회
    for i in range(start, N + 1):
        result.append(i)  # 숫자 추가
        backtrack(i + 1)  # 다음 숫자 선택 (중복 방지)
        result.pop()  # 선택 취소 (상태 복원)


------
backtrack(1)
def backtrack(path, choices):
    # 1. 종료 조건 확인 (해답 발견)
    if is_solution(path):
        save_result(path)
        return
    
    # 2. 가능한 모든 선택지 순회
    for choice in choices:
        # 3. 유효성 검사 (Pruning)
        if is_valid(choice, path):
            # 4. 선택 적용 (상태 변경)
            path.append(choice)
            
            # 5. 다음 단계 탐색 (재귀)
            backtrack(path, updated_choices)
            
            # 6. 선택 취소 (상태 복원)
            path.pop()


"""