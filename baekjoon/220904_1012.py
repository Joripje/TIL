# 1012 유기농 배추

# DFS를 사용해 풇이

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1
        
    worms = 0
    
    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                stack = [(i, j)]
                while stack:
                    v = stack.pop()
                    if farm[v[0]][v[1]]:
                        farm[v[0]][v[1]] = 0
                        for d in dxy:
                            nx = v[0] + d[0]
                            ny = v[1] + d[1]
                            if nx >= 0 and nx < N and ny >= 0 and ny < M and farm[nx][ny]:
                                stack.append((nx, ny))
                worms = worms + 1
                
    print(worms)