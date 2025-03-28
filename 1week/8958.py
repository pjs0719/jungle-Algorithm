N = int(input())

count = 1
score = 0 

for i in range(N):
    problem = input()
    count = 1
    score = 0 
    
    for j in problem:
        if "O" == j:
            score += count 
            count += 1
        else:
            count = 1
    print(score)      


## 흠.... 가우스 공식
# (len(x)+1) * (len(x)/2)라고 알고 있지만 len(x) * (len(x) + 1) // 2을 사용
for _ in range(int(input())):
    print(sum(len(x) * (len(x) + 1) // 2 for x in input().split('X')))
