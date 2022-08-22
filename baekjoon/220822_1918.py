# 1918 후위 표기식

# 스택을 이용해 후위 표기식으로 변환

notation = input()
stack = []
result = ''

for token in notation:
    if token.isalpha():
        result = result + token
    else:
        if token == '(':
            stack.append(token)

        elif token == ')':
            while stack[-1] != '(':
                result = result + stack.pop()
            stack.pop()

        elif token == '*' or token == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result = result + stack.pop()
            stack.append(token)

        else:
            while stack and stack[-1] != '(':
                result = result + stack.pop()
            stack.append(token)
                
while stack:
    result = result + stack.pop()
    
print(result)