# 1406 에디터

# 데이터의 입력,삭제가 커서의 왼쪽에서 이루어지므로 커서 왼쪽은 스택의 최상단
# 커서 기준으로 왼쪽 글자는 왼쪽 스택, 오른쪽 글자는 오른쪽 스택에
# 스택을 두개 사용해서 서로 옮겨 담음
# 합쳐서 출력

import sys

left_stack = list(sys.stdin.readline().strip())
m = int(input())

right_stack = []

for i in range(m):
    command = sys.stdin.readline().split()
    
    if command[0] == 'L': 
        if left_stack: # 커서 앞에 글자가 있으면 왼쪽으로 이동
            right_stack.append(left_stack.pop()) # 왼쪽 스택 데이터를 오른쪽 스택으로 옮김
            
    elif command[0] == 'D':
        if right_stack: # 커서 뒤에 글자가 있으면 오른쪽으로 이동
            left_stack.append(right_stack.pop()) # 오른쪽 스택 데이터를 왼쪽 스택으로 옮김
            
    elif command[0] == 'B':
        if left_stack: # 커서 앞에 글자가 있으면 삭제
            left_stack.pop()
        
    else:
        left_stack.append(command[1])

print(*left_stack, sep='',end='')
print(*right_stack[::-1], sep='',end='') # 오른쪽 글자 리스트는 순서를 뒤집어서 출력