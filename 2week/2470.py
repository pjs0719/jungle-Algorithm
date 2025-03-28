N = int(input())
T = list(map(int, input().split()))
T.sort()

result = float('inf')  # 최솟값을 찾기 위해 무한대로 초기화
ans = []

for idx, i in enumerate(T):
    low, hi = 0, len(T) - 1
    while low <= hi:
        mid = (low + hi) // 2

        if mid == idx:  # 같은 원소를 선택하는 경우 방지
            if mid + 1 <= hi:  # 오른쪽으로 한 칸 이동
                mid += 1
            else:  # 이동할 곳이 없으면 종료
                break

        if mid < 0 or mid >= len(T):  # 범위 체크
            break

        point = abs(i + T[mid])

        if result > point:
            result = point
            ans = [i, T[mid]]

        if i + T[mid] < 0:
            low = mid + 1  #
        else:
            hi = mid - 1  

print(*ans)  
