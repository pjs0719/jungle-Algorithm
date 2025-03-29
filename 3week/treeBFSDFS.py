# 트리를 표현하기 위한 Node 클래스 정의
class Node:
    def __init__(self, value):
        self.value = value  # 노드의 값
        self.children = []  # 자식 노드들을 저장할 리스트

    def add_child(self, child_node):
        self.children.append(child_node)  # 자식 노드를 추가하는 메서드


# BFS (너비 우선 탐색) 구현
def bfs(root):
    """
    BFS는 큐(Queue)를 사용하여 트리를 레벨 순서대로 탐색합니다.
    """
    if not root:  # 루트 노드가 None이면 탐색할 것이 없으므로 종료
        return

    queue = [root]  # 탐색을 위한 큐를 생성하고 루트 노드를 추가
    while queue:  # 큐가 빌 때까지 반복
        current_node = queue.pop(0)  # 큐의 첫 번째 노드를 꺼냄 (FIFO)
        print(current_node.value)  # 현재 노드의 값을 출력

        for child in current_node.children:  # 현재 노드의 자식들을 순회
            queue.append(child)  # 자식 노드를 큐에 추가


# DFS (깊이 우선 탐색) 구현 - 재귀 방식
def dfs_recursive(node):
    """
    DFS는 재귀적으로 각 노드를 방문하며 탐색합니다.
    """
    if not node:  # 현재 노드가 None이면 종료
        return

    print(node.value)  # 현재 노드의 값을 출력

    for child in node.children:  # 현재 노드의 자식들을 순회
        dfs_recursive(child)  # 재귀적으로 자식 노드를 탐색


# DFS (깊이 우선 탐색) 구현 - 스택 방식
def dfs_stack(root):
    """
    DFS는 스택(Stack)을 사용하여 트리를 깊이 우선으로 탐색할 수도 있습니다.
    """
    if not root:  # 루트 노드가 None이면 탐색할 것이 없으므로 종료
        return

    stack = [root]  # 탐색을 위한 스택을 생성하고 루트 노드를 추가
    while stack:  # 스택이 빌 때까지 반복
        current_node = stack.pop()  # 스택의 마지막 노드를 꺼냄 (LIFO)
        print(current_node.value)  # 현재 노드의 값을 출력

        for child in reversed(current_node.children):  
            # 자식들을 역순으로 추가하여 왼쪽부터 방문하도록 설정
            stack.append(child)


# 트리 생성 및 테스트 코드
if __name__ == "__main__":
    # 트리 구조 생성 (루트와 자식들)
    root = Node("A")  # 루트 노드 A 생성
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    root.add_child(node_b)
    root.add_child(node_c)
    node_b.add_child(node_d)
    node_b.add_child(node_e)
    node_c.add_child(node_f)

    print("BFS Traversal:")
    bfs(root)  # BFS 실행

    print("\nDFS Traversal (Recursive):")
    dfs_recursive(root)  # DFS (재귀 방식) 실행

    print("\nDFS Traversal (Stack):")
    dfs_stack(root)  # DFS (스택 방식) 실행
