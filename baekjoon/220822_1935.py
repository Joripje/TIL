# 1935 후위 표기식2

# 스택을 이용해 풀이
# 아스키 코드표로 영대문자를 숫자로 

N = int(input())
cal = input()
nums = [int(input()) for i in range(N)]
stack = []

for token in cal:
    if token == '*':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 * num1)
    elif token == '/':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 / num1)
    elif token == '+':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 + num1)
    elif token == '-':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 - num1)
        
    else:
        stack.append(nums[ord(token) - 65])
    
print(f'{stack.pop():.2f}')