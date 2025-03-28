N = []
ans = []

N = [int(input()) for _ in range(9)]
total = sum(N)

# 두 명의 난쟁이를 제외하여 합이 100이 되는 경우 찾기
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if total - N[i] - N[j] == 100:
            # 뒤에서부터 제거하여 인덱스 오류 방지
            del N[j]
            del N[i]
            found = True
            break
    if found:
        break

# 결과 출력
for num in sorted(N):
    print(num)

------


def solution(start):
    if len(ans) == 7:
        if sum(ans) == 100:
            for num in sorted(ans):
                print(num)
            exit()  # 프로그램 종료
        return

    for i in range(start, 9):
        ans.append(N[i])
        solution(i+1)
        ans.pop()
solution(0)

    
    

