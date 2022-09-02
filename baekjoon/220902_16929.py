# 16929 Two Dots

# DFS를 사용해 풀이

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())

dots = [list(input()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]  # dots와 동일한 크기의 방문 그래프
result = 0  # 사이클 존재 여부
stack = []


for i in range(N):  # dots를 순회하며 시작점 설정
    for j in range(M):
        if not visited[i][j]:  # 방문점이 아니라면 탐색 시작
            color = dots[i][j]  # 시작점의 색 저장
            stack.append((i, j, 1))  # 좌표와 방문 순서 저장
            
            # DFS 시작
            while stack:
                v = stack.pop()
                if not visited[v[0]][v[1]]:
                    visited[v[0]][v[1]] = v[2]
                    
                    for d in dxy:
                        nx = v[0] + d[0]
                        ny = v[1] + d[1]
                        
                        # dots 크기 안의 좌표면서 해당 점의 색이 시작점의 색과 같다면
                        if nx >= 0 and nx < N and ny >= 0 and ny < M and dots[nx][ny] == color:
                            # 이미 방문한 점이면서 현재 점에서 3번 이상 이동했었다면 사이클 조건 성립
                            if visited[nx][ny] and visited[nx][ny] + 3 <= v[2]:
                                result = 1
                                break
                            # 아니라면 스택에 좌표와 방문 순서 저장 저장
                            else:
                                stack.append((nx, ny, v[2] + 1))
                                
                    if result:
                        break
        if result:
            break
    if result:
        break


if result:
    print('Yes')
else:
    print('No')