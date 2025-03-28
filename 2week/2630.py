N = int(input())
T = []
for _ in range(N):
    row = list(map(int, input().split()))
    T.append(row)

def solution(n, arr):
    white = 0
    blue = 0
    
    # 전체 배열 검사
    if all(all(x == 1 for x in row) for row in arr):
        return (0, 1)
    elif all(all(x == 0 for x in row) for row in arr):
        return (1, 0)
    
    # 4분할 재귀 처리
    half = n // 2
    # 좌상단
    tl = [row[:half] for row in arr[:half]]
    w1, b1 = solution(half, tl)
    # 우상단
    tr = [row[half:] for row in arr[:half]]
    w2, b2 = solution(half, tr)
    # 좌하단
    bl = [row[:half] for row in arr[half:]]
    w3, b3 = solution(half, bl)
    # 우하단
    br = [row[half:] for row in arr[half:]]
    w4, b4 = solution(half, br)
    
    # 결과 합산
    total_white = w1 + w2 + w3 + w4
    total_blue = b1 + b2 + b3 + b4
    return (total_white, total_blue)

white, blue = solution(N, T)
print(white)
print(blue)
