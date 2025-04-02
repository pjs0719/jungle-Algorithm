N = int(input())
inout = list(input().strip())  
indices = {i + 1 for i, l in enumerate(inout) if l == '1'} # '1'이 있는 노드에서
walk = {i: [] for i in range(1, N + 1)}  
ans = 0

for _ in range(N - 1):
    a, b = map(int, input().split())
    walk[a].append(b)
    walk[b].append(a)


def dfs_recursive(walk, current, move, visited, count, course, results):
    visited[current] = True
    course.append(current)

    if count == move:
        results.append(course[:])  
        visited[current] = False  
        course.pop()
        return

    for neighbor in walk[current]:
        if not visited[neighbor]:
            
            if count < move - 1 and neighbor in indices:
                continue  

            dfs_recursive(walk, neighbor, move, visited, count + 1, course, results)

    visited[current] = False 
    course.pop()


for k in range(2, N):  # 이동 횟수
    for l in indices:  
        course = []
        visited = [False] * (N + 1)
        count = 1
        results = []  
        dfs_recursive(walk, l, k, visited, count, course, results)
        for m in results:
            if m[k-1] in indices:
                ans += 1

print(ans)