import sys
input = sys.stdin.readline 

N = int(input())

text = []

for _ in range(N):
    text.append(input().strip())

text.sort()

def solution(text):
    answer = []
    for i in range(51):  # 수정: 50 대신 len(text) 사용
        for k in range(len(text)):  # 수정: 문자열 최대 길이가 50이므로 51로 변경
            if len(text[k]) == i:
                answer.append(text[k])
    
    return answer

def solution2(text):
    answer = []
    for word in text:
        if word not in answer:
            answer.append(word)
    return answer
    

print('\n'.join(map(str, solution((solution2(text))))))
