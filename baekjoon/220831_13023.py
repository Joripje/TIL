# 13023 ABCDE


# dfs 함수 정의
def dfs(v, f):
    global result
    if f == 4:  # 이어지는 친구 관계가 4개라면
        result = 1  # 결과를 1로 바꾸고 종료
        return

    visited[v] = 1  # 방문처리
    for j in graph[v]:  # v와 연결된 노드 확인
        if not visited[j]:  # 해당 노드가 방문하지 않은 곳이라면
            dfs(v, f + 1)  # 해당 노드부터 시작하는 dfs 시작
            visited[j] = 0  # 가능한 모든 경로를 확인하기 위해 재귀에서 빠져나올 때 미방문 처리
        

N, M = map(int, input().split())

graph = {i: [] for i in range(N)}

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

result = 0

for i in range(N):
    visited = [0] * N
    dfs(i, 0)
    if result:
        break
    
print(result)