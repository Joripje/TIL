# 24480 깊이 우선 탐색 2
import sys

N, M, R = map(int,sys.stdin.readline().split())

gragh = [[] for i in range(N + 1)]

visited = [0] * (N + 1)

for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    gragh[u].append(v)
    gragh[v].append(u)

cnt = 0
stack = [R]

while stack:
    w = stack.pop()
    
    if visited[w] == 0:
        cnt = cnt + 1
        visited[w] = cnt
        
        for i in sorted(gragh[w]):
            if visited[i] == 0:
                stack.append(i)
    

for i in range(1, N + 1):
    print(visited[i])