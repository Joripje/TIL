# 2004 조합 0의 개수

# 팩토리얼의 소인수분해를 이용해 풀이
# nCr = n! / r! * (n-r)!
# 각 팩토리얼을 2와 5로 소인수분해해 개수를 센다

n, m = map(int, input().split())

p_2 = 0 # 분자의 2 개수
p_5 = 0 # 분자의 5 개수
m_2 = 0 # 분모의 2 개수
m_5 = 0 # 분모의 5 개수

# n! 소인수분해
num = n
while num != 0: # n의 몫이 없을때까지 나눔
    num = num // 2 # 주어진 숫자를 2로 나누고
    p_2 = p_2 + num # 몫을 분자의 2 개수에 더해줌
num = n
while num != 0: # n의 몫이 없을때까지 나눔
    num = num // 5 # 주어진 숫자를 5로 나누고
    p_5 = p_5 + num # 몫을 분자의 5 개수에 더해줌
    
# m! 소인수분해
num = m
while num != 0: # n의 몫이 없을때까지 나눔
    num = num // 2 # 주어진 숫자를 2로 나누고
    m_2 = m_2 + num # 몫을 분모의 2 개수에 더해줌
num = m
while num != 0: # n의 몫이 없을때까지 나눔
    num = num // 5 # 주어진 숫자를 5로 나누고
    m_5 = m_5 + num # 몫을 분모의 5 개수에 더해줌
    
# (n - m)! 소인수분해
num = n - m
while num != 0: # n의 몫이 없을때까지 나눔
    num = num // 2 # 주어진 숫자를 2로 나누고
    m_2 = m_2 + num # 몫을 분모의 2 개수에 더해줌
num = n - m
while num != 0: # n의 몫이 없을때까지 나눔
    num = num // 5 # 주어진 숫자를 5로 나누고
    m_5 = m_5 + num # 몫을 분모의 5 개수에 더해줌
    
# 2와 5의 곱으로 0이 만들어지므로 2와 5의 개수중 작은 수가 0의 개수
if p_2 > p_5:
    plus_0 = p_5
else:
    plus_0 = p_2
    
if m_2 > m_5:
    minus_0 = m_5
else:
    minus_0 = m_2
    
print(plus_0 - minus_0)