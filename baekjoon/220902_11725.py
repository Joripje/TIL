# 11725 트리의 부모 찾기

from collections import deque
N = int(input())

graph = { i:[] for i in range(1, N +1)}

for i in range(N - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [0] * (N + 1)
q = deque([1])
visited[1] = 1

while q:
    v = q.popleft()
    for w in graph[v]:
        if not visited[w]:
            q.append(w)
            visited[w] = visited[v] + 1

for i in range(2, N + 1):
    for j in graph[i]:
        if visited[j] == visited[i] - 1:
            print(j)