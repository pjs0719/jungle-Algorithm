N = int(input())

for i in range(N):
    print("*" * (i+1))




## 파이썬은 문자열을 특정 횟수만큼 반복하는 기능을 제공한다
for i in range(int(input())):print('*' * (i+1))


## 고급기능 활용
n,x,*a=map(int,open(0).read().split())
for i in a:i<x!=print(i)