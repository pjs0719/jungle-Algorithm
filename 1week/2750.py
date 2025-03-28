
N = []
for _ in range(int(input())):
    N.append(int(input()))

N.sort()

for i in N:
    print(i)

#리스트 컴프리헨션
N = sorted([int(input()) for _ in range(int(input()))])
for i in N:
    print(i)
