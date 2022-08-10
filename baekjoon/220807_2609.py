# 2609 최대공약수와 최소공배수

''' math 모듈 사용
import math

n, m = map(int, input().split())

print(math.gcd(n, m))
print(math.lcm(n, m))
'''
# 유클리드 호제법
# 재귀를 이용해 구현
n, m = map(int, input().split())  # n, m 입력받음
'''
if n >= m:
    a = n
    b = m

else:
    a = m
    b = n
'''
# 큰 수 a를 작은 수 b로 나누어 떨어지면 b는 a와 b의 최대공약수
# 나누어 떨어지지 않는다면 a와 b의 최대 공약수는 a / b 나머지와 b의 최대공약수와 같다
def gcd(a, b):
    
    if a % b == 0:
        return b
    
    else:
        return gcd(b, a % b)
    
print(gcd(n, m))
print(int(n * m / gcd(n, m)))  # 최소공배수는 두 수를 서로소가 될 때까지 나눈 수들과 그 서로소의 곱