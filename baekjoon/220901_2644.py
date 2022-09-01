# 2644 촌수계산

N = int(input())
family = {i : [] for i in range(1, N + 1)}
a, b = map(int, input().split())
M = int(input())
for i in range(M):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
    
visited = [0] * (N + 1)
stack = [(a, 1)]
chon = -1
while stack:
    v = stack.pop()
    if not visited[v[0]]:
        visited[v[0]] = v[1]
        for w in family[v[0]]:
            if not visited[w]:
                if w == b:
                    chon = v[1]
                    break
                else:
                    stack.append((w, v[1] + 1))
    if chon != -1:
        break

print(chon)