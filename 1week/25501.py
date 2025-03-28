T = int(input())


def recursion(s, l, r):
    global count
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        count += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count += 1
    return recursion(s, 0, len(s)-1)


for _ in range(T):
   count = 0
   print(isPalindrome(input()), count)
  
---

def recursion(s, l, r, count):
    count[0] += 1  # 재귀 호출 횟수 증가
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1, count)

def isPalindrome(s):
    count = [0]  # 재귀 호출 횟수를 저장할 리스트
    result = recursion(s, 0, len(s) - 1, count)
    return result, count[0]

# 입력 처리
n = int(input())  # 테스트 케이스 개수 입력
for _ in range(n):
    s = input().strip()  # 문자열 입력
    result, call_count = isPalindrome(s)
    print(result, call_count)
