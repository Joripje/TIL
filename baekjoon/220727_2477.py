# 2477 참외밭

n = int(input())

move_list = [tuple(input().split(' ')) for i in range(6)] # 이동 리스트를 튜플로 받아 리스트 저장
direction_list = [] # 이동방향 리스트

# 큰 사각형 넓이를 구할 때 사용할 임의의 변수
X = []
idx_list = []

# 이동 횟수 세기 
for move in move_list:
    direction_list.append(move[0])
    
for direction in direction_list:
    if direction_list.count(direction) == 1: # 1번 존재하는 방향이라면
        X.append(direction)

# 큰 사각형 넓이 구하기
# 이동횟수가 1인 방향의 이동거리를 리스트에 저장
for x in X:
    for idx, move in enumerate(move_list):
        if move[0] == x: 
            idx_list.append(idx)
            
            
big_nemo = int(move_list[idx_list[0]][1]) * int(move_list[idx_list[1]][1])

# 작은 사각형 넓이 구하기

small_idx = []

if idx_list == [0, 1]:
    small_idx = [3, 4]

elif idx_list == [1, 2]:
    small_idx = [4, 5]

elif idx_list == [2, 3]:
    small_idx = [0, 5]

elif idx_list == [3, 4]:
    small_idx = [0, 1]
    
elif idx_list == [4, 5]:
    small_idx = [1, 2]
    
else:
    small_idx = [2, 3]
    
small_nemo = int(move_list[small_idx[0]][1]) * int(move_list[small_idx[1]][1])

print((big_nemo - small_nemo) * n)