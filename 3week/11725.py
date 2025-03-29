import sys

def solve():
    # 입력값: 트리의 노드 개수
    n = int(sys.stdin.readline())
    
    # 인접 리스트 초기화 (노드 번호는 1부터 시작하므로 n+1 크기로 생성)
    adj = [[] for _ in range(n + 1)]
    
    # 각 노드의 부모 정보를 저장할 리스트 초기화
    p = [0] * (n + 1)

    # 간선 정보 입력받아 인접 리스트 생성
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)  # u와 v를 서로 연결
        adj[v].append(u)

    # 깊이 우선 탐색(DFS) 함수 정의
    def dfs(cur):
        # 현재 노드(cur)에 연결된 모든 인접 노드(nxt)를 순회
        for nxt in adj[cur]:
            # 부모 노드로 돌아가는 경우는 건너뜀
            if p[cur] == nxt:
                continue
            # 현재 노드를 다음 노드의 부모로 설정
            p[nxt] = cur
            # 다음 노드에 대해 재귀적으로 DFS 호출
            dfs(nxt)

    # 루트 노드(1번 노드)부터 DFS 시작
    dfs(1)

    # 결과 출력: 각 노드(2번부터 n번까지)의 부모 노드 출력
    for i in range(2, n + 1):
        print(p[i])

# 문제 해결 함수 호출
solve()




import sys

class Tree:
    def __init__(self, n):
        # 트리의 노드 개수
        self.n = n
        # 인접 리스트 초기화
        self.adj = [[] for _ in range(n + 1)]
        # 각 노드의 부모 정보를 저장할 리스트 초기화
        self.parent = [0] * (n + 1)

    def add_edge(self, u, v):
        # 간선 정보를 인접 리스트에 추가
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, cur):
        # 현재 노드(cur)에 연결된 모든 인접 노드(nxt)를 순회
        for nxt in self.adj[cur]:
            # 부모 노드로 돌아가는 경우는 건너뜀
            if self.parent[cur] == nxt:
                continue
            # 현재 노드를 다음 노드의 부모로 설정
            self.parent[nxt] = cur
            # 다음 노드에 대해 재귀적으로 DFS 호출
            self.dfs(nxt)

    def find_parents(self):
        # 루트 노드(1번 노드)부터 DFS 시작
        self.dfs(1)
        # 결과 반환: 각 노드(2번부터 n번까지)의 부모 노드 리스트
        return self.parent[2:]

def main():
    # 입력 처리: 트리의 노드 개수
    n = int(sys.stdin.readline())
    
    # Tree 클래스 인스턴스 생성
    tree = Tree(n)
    
    # 간선 정보 입력받아 트리에 추가
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        tree.add_edge(u, v)
    
    # 각 노드의 부모 정보 찾기
    parents = tree.find_parents()
    
    # 결과 출력: 2번 노드부터 n번 노드까지의 부모 정보 출력
    for parent in parents:
        print(parent)

# 프로그램 실행
if __name__ == "__main__":
    main()
