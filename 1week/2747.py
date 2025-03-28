N = int(input())
a = [0, 1]
b = 0

for i in range(N-1):
    a.append(a[i]+a[i+1])
    

print(a[N])





def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_sequence(n):
    return [fib_recursive(i) for i in range(n+1)]

# 사용 예시
n = 10
result = fib_sequence(n)
print(" ".join(map(str, result)))


