# 10773 제로

n = int(input())


# 숫자를 저장할 리스트와 명령어 리스트를 생성
nums = []
commands = [int(input()) for i in range(n)]

for command in commands: # 명령어 리스트를 순회
    if command:
        nums.append(command) # 명령어가 0이 아니라면 숫자 리스트에 숫자 추가
    else:
        nums.pop() # 명령어가 0이라면 마지막에 입력된 숫자 제거
        
print(sum(nums))