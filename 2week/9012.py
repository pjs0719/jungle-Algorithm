N = int(input())
for _ in range(N):
    VPS = input()
    stack = []
    is_valid = True
    for char in VPS:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                is_valid = False
                break
            stack.pop()
    
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")
