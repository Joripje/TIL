# 10799 쇠막대기

# 레이저의 기호 변환
# 여는 괄호로 막대가 들어오면 카운트 + 1
# 레이저를 만나면 들어온 막대를 잘라 막대만큼 결과 추가
# 닫는 괄호로 막대가 끝나면 카운트 + 1 끄트머리 결과 추가

iron_laser = input()

iron_laser = iron_laser.replace('()', '/') # 레이저 기호 변환

count = 0
result = 0

for iron in iron_laser:
    if iron == '/': 
        result = result + count # 레이저를 만나면 현재 막대 개수만큼 결과 추가
        
    elif iron == '(':
        count = count + 1 # 막대가 들어오면 막대 카운트 +1
        
    elif iron == ')':
        count = count - 1
        result = result + 1 # 막대가 끝나면 막대 카운트 -1, 결과에 + 1
        
print(result)