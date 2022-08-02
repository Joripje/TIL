# 1874 스택수열

# 스택의 맨 위가 현재 입력해야 하는 수라면 pop
# 그렇지 않다면 push
# 스택을 두개 써서 수열을 만들어보기?
# 전부 시도후 스택이 비어있다면 성공

n = int(input())

stack = [] # 새로운 스택
command = [] # 명령을 담아둘 스택
count = 0 # n까지 숫자를 넣기 위한 카운트
num_count = 0 # 현재 시도중인 숫자 카운트

nums = [int(input()) for i in range(n)]

while num_count != n and count < n + 1: # n까지의 정수만 시도, 수열을 끝까지 돌면 끝
    
    if stack: # 스택이 비어있지 않다면 수열을 채울수 있는지 판별
        
        if nums[num_count] == stack[-1]: # 스택의 맨 위의 숫자가 입력해야 되는 숫자라면
            stack.pop()
            command.append('-')
            num_count = num_count + 1 # pop, 다음 숫자로 넘어감
            
        else: # 입력해야 되는 숫자가 아니라면
            stack.append(count + 1) 
            command.append('+')
            count = count + 1 # push, 다음 숫자를 판별
        
    else: # 스택이 비어있다면 정수를 넣어주고 숫자 카운트를 올린다 (push)
        stack.append(count + 1)
        command.append('+')
        count = count + 1
        

if stack: # 스택이 비어있지 않다면 실패
    print('NO')
    
else: # 비워졌다면 성공
    for command in command:
        print(command)