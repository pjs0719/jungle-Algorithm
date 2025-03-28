import sys



a = int(sys.stdin.readline())
N = []
c = [0] * 10001 
answer = [0] * a

for _ in range(a):
    tem = int(sys.stdin.readline().strip())
    N.append(tem)
    c[tem] += 1 
#배열 입력 받고, 더하기 작업

for k in range(1,len(c)):
    c[k] += c[k-1]
#누적 더하기 작업


for i in range(a-1, -1, -1):
    num = N[i]
    c[num] -= 1
    answer[c[num]] = N[i]
#누적 값에 따른 배열 생성


for sol in answer:
    print(sol)
