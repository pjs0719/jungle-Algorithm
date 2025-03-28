num = []

for _ in range(9):
    num.append(int(input()))

max = 0
count = 1

for i in num:
    if max < i:
        max = i
        count_p = count
    count += 1  

print(max)
print(count_p)

## max와 리스트 컴프리헨션
numbers = [int(input()) for _ in range(9)]
max_value = max(numbers)
max_index = numbers.index(max_value) + 1

print(max_value)
print(max_index)

## 줄이기
for _ in range(9):
    num.append(int(input()))

-> numbers = [int(input()) for _ in range(9)]