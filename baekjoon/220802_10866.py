# 10866번 덱

# 명령을 입력받은 뒤 각 명령 처리
n = int(input())

commands = [input() for i in range(n)]

deque = []
size = 0

for command in commands:
    
    if command == 'size':
        print(size)
        
    elif command == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
            
    elif command == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    
    elif command == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
            
    elif command[:6] == 'push_b':
        deque.append(command.split(' ')[1])
        size = size + 1
        
    elif command[:6] == 'push_f':
        deque.insert(0, command.split(' ')[1])
        size = size + 1
        
    elif command[:6] == 'pop_fr':
        if deque:
            print(deque.pop(0))
            size = size - 1
        else:
            print(-1)
    
    else:
        if deque:
            print(deque.pop(-1))
            size = size - 1
        else:
            print(-1)