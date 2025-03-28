num = 1
count = [0,0,0,0,0,0,0,0,0,0]

for i in range(3):
    num *= int(input()) 

str_num = str(num)

for j in range(10):
    for k in str_num:
        if str(j) == k:
            count[j] += 1

for i in count:
    print(i)


