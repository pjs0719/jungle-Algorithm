S = input()
boom = input()
ans = []

for char in S:
    ans.append(char)  # 한 글자씩 스택에 추가

    # 스택 끝부분이 boom과 같다면 삭제
    if len(ans) >= len(boom) and ans[-len(boom):] == list(boom):
        del ans[-len(boom):]

# 결과 출력
print("FRULA" if not ans else "".join(ans))
