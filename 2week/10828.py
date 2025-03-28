import sys
input = sys.stdin.readline

# 스택 초기화
stack = []

# 명령 개수 입력
n = int(input())

for _ in range(n):
    command = input().strip().split()

    if command[0] == "push":
        # push X: X를 스택에 추가
        stack.append(int(command[1]))
    elif command[0] == "pop":
        # pop: 스택의 맨 위 요소 제거 및 출력, 없으면 -1 출력
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        # size: 스택의 크기 출력
        print(len(stack))
    elif command[0] == "empty":
        # empty: 스택이 비어있으면 1, 아니면 0 출력
        print(1 if not stack else 0)
    elif command[0] == "top":
        # top: 스택의 맨 위 요소 출력, 없으면 -1 출력
        if stack:
            print(stack[-1])
        else:
            print(-1)

