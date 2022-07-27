# 10828 스택

n = int(input())

stack = [] # 스택 리스트
command_list = [input() for i in range(n)] # 명령어 리스트 생성

for command in command_list: # 명령어 리스트를 순회
    
    if command[:2] == 'pu': # push
        stack.append(command.split(' ')[1])
        
    elif command[:2] == 'po': # pop
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif command[:2] == 'si': # size
        print(len(stack))
    
    elif command[:2] == 'em': # empty
        if stack:
            print(0)
        else:
            print(1)
    
    else: # top
        if stack:
            print(stack[-1])
        else:
            print(-1)