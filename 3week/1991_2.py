class Node:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, value, left=None, right=None):
        self.value = value  # 노드의 값
        self.left = left    # 왼쪽 자식 노드
        self.right = right  # 오른쪽 자식 노드

def build_tree():
    # 입력을 받아 이진 트리를 구성하는 함수
    n = int(input())  # 노드의 개수 입력
    # A부터 Z까지의 알파벳에 해당하는 노드 생성
    nodes = {chr(ord('A') + i): Node(chr(ord('A') + i)) for i in range(n)}
    
    for _ in range(n):
        # 각 노드와 자식 정보를 입력받음
        value, left, right = input().split()
        current_node = nodes[value]  # 현재 노드 가져오기
        # 왼쪽 자식 설정 ('.'은 None으로 처리)
        current_node.left = nodes[left] if left != '.' else None
        # 오른쪽 자식 설정 ('.'은 None으로 처리)
        current_node.right = nodes[right] if right != '.' else None
    
    return nodes['A']  # 항상 A가 루트 노드이므로 반환

def preorder(node, result):
    # 전위 순회: (루트) → (왼쪽 자식) → (오른쪽 자식)
    if node is None:
        return  # 노드가 없으면 종료
    result.append(node.value)  # 현재 노드 값 추가
    preorder(node.left, result)  # 왼쪽 서브트리 방문
    preorder(node.right, result)  # 오른쪽 서브트리 방문

def inorder(node, result):
    # 중위 순회: (왼쪽 자식) → (루트) → (오른쪽 자식)
    if node is None:
        return  # 노드가 없으면 종료
    inorder(node.left, result)  # 왼쪽 서브트리 방문
    result.append(node.value)  # 현재 노드 값 추가
    inorder(node.right, result)  # 오른쪽 서브트리 방문

def postorder(node, result):
    # 후위 순회: (왼쪽 자식) → (오른쪽 자식) → (루트)
    if node is None:
        return  # 노드가 없으면 종료
    postorder(node.left, result)  # 왼쪽 서브트리 방문
    postorder(node.right, result)  # 오른쪽 서브트리 방문
    result.append(node.value)  # 현재 노드 값 추가

# 트리 구성
root = build_tree()

# 전위 순회 결과 계산
pre_result = []
preorder(root, pre_result)

# 중위 순회 결과 계산
in_result = []
inorder(root, in_result)

# 후위 순회 결과 계산
post_result = []
postorder(root, post_result)

# 결과 출력: 리스트를 문자열로 변환하여 출력
print(''.join(pre_result))  # 전위 순회 결과 출력
print(''.join(in_result))   # 중위 순회 결과 출력
print(''.join(post_result))  # 후위 순회 결과 출력
