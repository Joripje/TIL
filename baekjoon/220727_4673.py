# 4673 셀프 넘버

def d(n): # d(n) 수열
    total = n # 총합에 자기 자신 n을 더함
    
    for num in str(n): # n을 문자열로 만들어 순회
        total = total + int(num) # 각 자리수를 더함
        
    return total

not_self = [] # 셀프 넘버가 아닌 숫자 리스트

for i in range(1, 10001): # 임의의 큰 정수까지 반복하며
    if (d(i)) <= 10000: # 10000 이하의 셀프 넘버가 아닌 숫자라면
        not_self.append(d(i)) # 셀프 넘버가 아닌 리스트에 추가
        
self_list = []

for i in range(1, 10001): # 1부터 10000까지 정수
    if i not in not_self: # 셀프 넘버가 아니라면
        self_list.append(i) # 셀프 넘버 리스트에 추가
        
        
# 문제 조건에 맞게 출력        
for num in self_list:
    print(num)