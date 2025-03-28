import sys
input = sys.stdin.readline

stack = []
# 명령 개수 입력
n = int(input())
for _ in range(n):
    K = int(input())
    if K == 0:
        stack.pop()
    else:
        stack.append(K)

print(sum(stack))