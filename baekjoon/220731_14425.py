# 14425 문자열 집합

n, m = map(int, input().split(' '))

s_words = [input() for i in range(n)]
check_words = [input() for i in range(m)]

s_dict = {}

for word in s_words:
    s_dict[word] = 1 # 같은 문자열이 주어지지 않으므로 딕셔너리 키로 사용
    
count = 0

for word in check_words:
    if s_dict.get(word): # 검사 문자열이 S에 포함되어 key에 접근할 수 있다면
        count = count + 1 # count 1 증가
        
print(count)