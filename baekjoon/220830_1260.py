# 1260 DFS와 BFS
# 반복문을 통해 DFS와 BFS 구현
from collections import deque

N, M, V = map(int, input().split())

gragh = [[0] * (N + 1) for i in range(N + 1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    gragh[n1][n2] = 1
    gragh[n2][n1] = 1
    
# DFS
visited = [0] * (N + 1)
stack = [V]
dfs = []
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = 1
        dfs.append(v)
        for i in range(N, 0, -1):
            if gragh[v][i] and not visited[i]:
                stack.append(i)
                

# BFS
visited = [0] * (N + 1)
queue = deque([V])
visited[V] = 1
bfs = [V]
while queue:
    v = queue.popleft()
    for i in range(N + 1):
        if gragh[v][i] and not visited[i]:
            queue.append(i)
            visited[i] = 1
            bfs.append(i)
            
print(*dfs, sep=' ')
print(*bfs, sep=' ')