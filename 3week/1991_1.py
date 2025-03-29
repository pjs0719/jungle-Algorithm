# 트리의 노드 개수 입력받기
n = int(input())

# 왼쪽 자식 노드와 오른쪽 자식 노드를 저장할 딕셔너리 초기화
lc = {}  # 왼쪽 자식 노드
rc = {}  # 오른쪽 자식 노드

# 트리 구조 입력받기
for _ in range(n):
    # 현재 노드(c), 왼쪽 자식(l), 오른쪽 자식(r) 입력받기
    c, l, r = input().split()
    cur = ord(c) - ord('A') + 1  # 문자 'A'를 1로 변환 (1-based 인덱싱)
    
    # 왼쪽 자식이 존재하면 lc 딕셔너리에 저장
    if l != '.':  # '.'은 자식이 없음을 의미
        lc[cur] = ord(l) - ord('A') + 1
    
    # 오른쪽 자식이 존재하면 rc 딕셔너리에 저장
    if r != '.':
        rc[cur] = ord(r) - ord('A') + 1

# 전위 순회 함수 (Preorder Traversal: V → L → R)
def preorder(cur):
    # 현재 노드 출력 (문자로 변환)
    print(chr(cur + ord('A') - 1), end='')
    
    # 왼쪽 자식이 존재하면 재귀 호출
    if lc.get(cur, 0):  # lc 딕셔너리에 현재 노드의 왼쪽 자식이 있는지 확인
        preorder(lc[cur])
    
    # 오른쪽 자식이 존재하면 재귀 호출
    if rc.get(cur, 0):  # rc 딕셔너리에 현재 노드의 오른쪽 자식이 있는지 확인
        preorder(rc[cur])

# 중위 순회 함수 (Inorder Traversal: L → V → R)
def inorder(cur):
    # 왼쪽 자식이 존재하면 재귀 호출
    if lc.get(cur, 0):
        inorder(lc[cur])
    
    # 현재 노드 출력 (문자로 변환)
    print(chr(cur + ord('A') - 1), end='')
    
    # 오른쪽 자식이 존재하면 재귀 호출
    if rc.get(cur, 0):
        inorder(rc[cur])

# 후위 순회 함수 (Postorder Traversal: L → R → V)
def postorder(cur):
    # 왼쪽 자식이 존재하면 재귀 호출
    if lc.get(cur, 0):
        postorder(lc[cur])
    
    # 오른쪽 자식이 존재하면 재귀 호출
    if rc.get(cur, 0):
        postorder(rc[cur])
    
    # 현재 노드 출력 (문자로 변환)
    print(chr(cur + ord('A') - 1), end='')

# 루트 노드를 기준으로 각각의 순회 결과 출력
preorder(1)   # 전위 순회 결과 출력
print()       # 줄바꿈
inorder(1)    # 중위 순회 결과 출력
print()       # 줄바꿈
postorder(1)  # 후위 순회 결과 출력
print()       # 줄바꿈
