# 9012 괄호

n = int(input())
pstrings = [input() for i in range(n)]

# 괄호 문자열에서 한쌍의 괄호 조합 '()'을 계속해서 지운다
# 이를 반복, VPS라면 빈 문자열이 되며 VPS가 아니라면 괄호가 남는다
for pstring in pstrings:
    pstr = pstring # VPS 판별을 위한 괄호 문자열
    
    # '()'이 존재한다면 계속 지운다
    while pstr.find('()') != -1:
        pstr = pstr.replace('()', '', 1)
    
    # 결과가 빈 문자열이라면 VPS, 아니라면 VPS가 아님
    if pstr == '':
        print('YES')
    
    else:
        print('NO')