N = int(input())

for i in range(1, 10):
    print( N, "*", i, "=", i*N)



# 덧셈을 이용한 방식
a = b = int(input())
exec("print(a,'*',b//a,'=',b);b+=a;" * 9)
