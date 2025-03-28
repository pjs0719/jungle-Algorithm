N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
S = list(map(int, input().split()))

def solution(A,i,low,hi):
    mid = (low+hi)//2
    if low > hi:
        return 0

    if A[mid] == i:
        return 1
    elif i > A[mid]:
        return solution(A, i, mid + 1, hi)
    else:
        return solution(A, i, low, mid - 1)




for i in S:
    print(solution(A, i, 0, len(A)-1))

---

def solution(arr, such):
    low, hi = 0, len(arr)-1

    while low <= hi:
        mid = (low + hi) //2
        if arr[mid] == such:
            return 1
        elif such > arr[mid]:
            low = mid+1      
        elif such < arr[mid]:
            hi = mid-1

    return 0

for i in S:
    print(solution(A, i))


