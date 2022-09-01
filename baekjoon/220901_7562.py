# 7562 나이트의 이동

from collections import deque

# 나이트의 이동 가능 좌표(8방향)
knight = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


# 나이트의 이동 가능 여부 확인
def is_possible(x, y):
    if x >= 0 and x < l and y >= 0 and y < l and plate[x][y] == 0:
        return True
    else:
        return False


T = int(input())
for tc in range(T):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    plate = [[0] * l for i in range(l)]
    target = (x2, y2)

    queue = deque([(x1, y1)])
    plate[x1][y1] = 1

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