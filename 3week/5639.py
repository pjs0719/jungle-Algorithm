import sys
sys.setrecursionlimit(10**6)  

tree = [int(line.rstrip()) for line in sys.stdin.readlines()]

def postorder(tree):
    if not tree:  
        return
        
    root = tree[0]
    right_start = len(tree)  

    
    for i in range(1, len(tree)):
        if tree[i] > root:
            right_start = i
            break
    
    # 왼쪽과 오른쪽 서브트리로 나눠 재귀 호출
    postorder(tree[1:right_start])  # 왼쪽 서브트리
    postorder(tree[right_start:])   # 오른쪽 서브트리
    print(root)  # 루트 출력 (후위 순서)

postorder(tree)
