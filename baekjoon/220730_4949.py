# 4949 균형잡힌 세상

# 주어진 문장을 괄호만으로 이루어진 문장으로 변환
strings = []

while True:
    string = input()
    ps = ''
    if string != '.':
        for char in string[:-1]:
            if char == '(' or char == ')' or char == '[' or char == ']':
                ps = ps + char
        strings.append(ps)
    else:
        break
        
# 괄호만으로 이루어진 문장들을 순회하며 균형을 이루는지 확인
for string in strings:
    
    while string.find('[]') != -1 or string.find('()') != -1: # '[]' 혹은 '()' 가 존재한다면 괄호를 지운다
        string = string.replace('[]', '', 1)
        string = string.replace('()', '', 1)
    
    if string == '':
        print('yes')
        
    else:
        print('no')