count = 0
for i in range(int(input())):
    num = i + 1
    be = list(map(int, str(num)))
    
    if len(be) == 1 or len(be) == 2:
        count += 1
    else:
        diff = be[1] - be[0]
        is_arithmetic = all(be[j] - be[j-1] == diff for j in range(2, len(be)))
        if is_arithmetic:
            count += 1

print(count)
