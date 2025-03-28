def push(arr, x):
    arr.append(x)
    idx = len(arr) - 1  # 새로 추가된 요소의 인덱스
    
    # Bubble-up: 부모와 비교하며 힙 속성 복구
    while idx > 1:
        parent_idx = idx // 2
        if arr[idx] > arr[parent_idx]:
            arr[idx], arr[parent_idx] = arr[parent_idx], arr[idx]
            idx = parent_idx
        else:
            break
    return arr

def max_pop(arr):
    if len(arr) <= 1:
        print(0)
        return arr
    
    max_val = arr[1]
    last = arr.pop()
    
    if len(arr) > 1:
        arr[1] = last
        # Heapify-down: 자식과 비교하며 힙 속성 복구
        current = 1
        while True:
            left = 2 * current
            right = 2 * current + 1
            largest = current
            
            if left < len(arr) and arr[left] > arr[largest]:
                largest = left
            if right < len(arr) and arr[right] > arr[largest]:
                largest = right
                
            if largest != current:
                arr[current], arr[largest] = arr[largest], arr[current]
                current = largest
            else:
                break
    else:
        arr = [0]
        
    print(max_val)
    return arr

arr = [0]
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        arr = max_pop(arr)
    else:
        arr = push(arr, x)
