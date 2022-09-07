# 16948 데스 나이트

from collections import deque

# 나이트의 이동 가능 좌표(6방향)
knight = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]


# 나이트의 이동 가능 여부 확인
def is_possible(x, y):
    if x >= 0 and x < l and y >= 0 and y < l and plate[x][y] == 0:
        return True
    else:
        return False



l = int(input())
x1, y1 , x2, y2 = map(int, input().split())
plate = [[0] * l for i in range(l)]
target = (x2, y2)

queue = deque([(x1, y1)])
plate[x1][y1] = 1
result = 0

while queue:
    v = queue.popleft()
    if v == target:
        result = plate[v[0]][v[1]]
        break
    else:
        for move in knight:
            nx = v[0] + move[0]
            ny = v[1] + move[1]
            if is_possible(nx, ny):
                plate[nx][ny] = plate[v[0]][v[1]] + 1
                queue.append((nx, ny))

print(result - 1)