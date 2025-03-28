T = []
ans = []
for _ in range(5):
    T.append(int(input()))

def solution(low,hi,i):
    mid = (low + hi) // 2




for i in T
    solution(0,4,i)
print(sum(T)//5)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 중앙값을 피벗으로 선택
    left = []
    middle = []
    right = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return quick_sort(left) + middle + quick_sort(right)