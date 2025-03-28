
for _ in range(int(input())): 
    R, S = input().split()
    result = []
    R = int(R)
    for i in S:
        for _ in range(R):
            result.append(i)

    print(''.join(result))


#리스트 컴프리헨션 + join
for _ in range(int(input())):
    R, S = input().split()
    R = int(R)
    result = ''.join(char * R for char in S)
    print(result)
