def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # 마지막 요소를 피봇으로 선택
    less = []
    greater = []
    
    for x in arr[:-1]:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    
    return quick_sort(less) + [pivot] + quick_sort(greater)
