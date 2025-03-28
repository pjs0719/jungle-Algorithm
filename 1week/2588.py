num1 = int(input())
num2 = int(input())


num1_1 = num1 % 10
num1_10 = ((num1 // 10) %10) * 10
num1_100 = ((num1//10)//10) * 100

#여기서 곱하는 대신 p1을 계산할 때 10,100을 곱해도 상관 없음
#num1_10의 경우 (num1%100)//10으로 써도 십의 자리 수를 구할 수 있음

num2_1 = num2 % 10 
num2_10 = ((num2 // 10) % 10)
num2_100 = ((num2 // 10)//10)

p1 = (num2_1 * num1_1) + (num2_1 * num1_10) + (num2_1 * num1_100)
p2 = (num2_10 * num1_1) + (num2_10 * num1_10) + (num2_10 * num1_100)
p3 = (num2_100 * num1_1) + (num2_100 * num1_10) + (num2_100 * num1_100)



print(p1)
print(p2)
print(p3)
print(num1*num2)


