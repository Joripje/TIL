# 2609 최대공약수와 최소공배수

''' math 모듈 사용
import math

n, m = map(int, input().split())

print(math.gcd(n, m))
print(math.lcm(n, m))
'''
# 유클리드 호제법
# 재귀를 이용해 구현

n, m = map(int, input().split())
    
def gcd(a, b):
    
    if a % b == 0:
        return b
    
    else:
        return gcd(b, a % b)
    
print(gcd(n, m))
print(int(n * m / gcd(n, m))) # 최소공배수 