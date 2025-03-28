N = int(input())
dec = list(map(int, input().split()))
count = 0

for i in dec:
    if i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17 or i == 19 or i == 23 or i == 29 or i == 31:
        count += 1
        
    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) and (i % 11 != 0)and (i % 13 != 0) and (i % 17 != 0) and (i % 19!= 0) and (i % 23 != 0) and (i % 29 != 0) and (i % 31 != 0) and ( i != 1):
        count += 1
       
    
print(count)


#각 숫자의 루트를 적용하여 그 숫자를 소인수 분해?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # √n까지 검사
        if n % i == 0:
            return False
    return True

N = int(input())
dec = list(map(int, input().split()))
count = 0

for num in dec:
    if is_prime(num):
        count += 1

print(count)
