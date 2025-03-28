# 입력받기: 배열 A의 크기 N
N = int(input())

# 배열 A를 입력받아 정렬
A = sorted(list(map(int, input().split())))

# 입력받기: 탐색할 숫자의 개수 M
M = int(input())

# 탐색할 숫자 리스트 S를 입력받음
S = list(map(int, input().split()))

# 첫 번째 등장 위치를 찾는 함수 (Lower Bound)
def find_first(arr, target):
    left, right = 0, len(arr) - 1  # 탐색 범위 초기화
    first = -1  # 첫 번째 위치를 저장할 변수 (-1은 값이 없음을 의미)
    while left <= right:  # 탐색 범위가 유효할 동안 반복
        mid = (left + right) // 2  # 중간 인덱스 계산
        if arr[mid] >= target:  # 중간 값이 목표 값 이상일 경우
            if arr[mid] == target:  # 목표 값을 찾았을 때 위치 저장
                first = mid
            right = mid - 1  # 왼쪽 부분으로 탐색 범위 축소
        else:
            left = mid + 1  # 오른쪽 부분으로 탐색 범위 축소
    return first  # 첫 번째 등장 위치 반환


# 마지막 등장 위치를 찾는 함수 (Upper Bound)
def find_last(arr, target):
    left, right = 0, len(arr) - 1  # 탐색 범위 초기화
    last = -1  # 마지막 위치를 저장할 변수 (-1은 값이 없음을 의미)
    while left <= right:  # 탐색 범위가 유효할 동안 반복
        mid = (left + right) // 2  # 중간 인덱스 계산
        if arr[mid] <= target:  # 중간 값이 목표 값 이하일 경우
            if arr[mid] == target:  # 목표 값을 찾았을 때 위치 저장
                last = mid
            left = mid + 1  # 오른쪽 부분으로 탐색 범위 축소
        else:
            right = mid - 1  # 왼쪽 부분으로 탐색 범위 축소
    return last  # 마지막 등장 위치 반환

# 특정 값의 등장 횟수를 계산하는 함수
def count_occurrences(arr, target):
    first = find_first(arr, target)  # 첫 번째 등장 위치 찾기
    if first == -1:  # 값이 없으면 등장 횟수는 0
        return 0
    last = find_last(arr, target)  # 마지막 등장 위치 찾기
    return last - first + 1  # 등장 횟수 계산 (첫 번째와 마지막 위치의 차이 +1)

# S의 각 숫자에 대해 A에서의 등장 횟수를 출력
for num in S:
    print(count_occurrences(A, num))
