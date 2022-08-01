# 10845 큐

# 명령을 입력받은 뒤 각 명령 처리
import sys

n = int(input())

commands = [input() for i in range(n)]

queue = []

for command in commands:

    if command == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
        
    elif command == 'size':
        print(len(queue))
        
    elif command == 'empty':
        if queue:
            print(0)
            
        else:
            print(1)
    
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
            
    else:
        queue.append(command.split(' ')[1])