N, X = map(int , input().split())
A = list(map(int , input().split()))

a = 0
answer=[] 
 
for j in A:
    if j < X:
        answer.append(j) 

print(*answer)

##List Comprehension
# [만들 것 for 항목 in 가져올 곳 if 조건]
answer = [j for j in A if j < X]
