
a, b = input().split()
ar = []
br = []
k = 2

for _ in range(3):
    ar.append(a[k])
    br.append(b[k])
    k -= 1

a = ''.join(ar)
b = ''.join(br)

if int(a) > int(b):
    answer = int(a)
else:
    answer = int(b)

print(answer)


## 함수를 사용하여 짧게 풀기
a, b = input().split()
a = int(a[::-1])  # 문자열을 뒤집고 정수로 변환
b = int(b[::-1])  # 문자열을 뒤집고 정수로 변환

print(max(a, b))  # 두 수 중 큰 값 출력
