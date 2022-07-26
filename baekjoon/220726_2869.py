# 2869 달팽이는 올라가고 싶다


''' 숫자가 커지는 경우 연산이 매우 오래 걸리는 문제 발생
# a: 낮에 올라가는 높이, b: 밤에 미끄러지는 높이, v: 목표 높이
a, b, v = map(int, input().split(' '))

day = 1 # 1일부터 시작
h = a # 올라간 거리 설정

while h < v: # 올라간 거리가 목표높이보다 높아질때까지 반복
    h = h - b # 밤에 미끄러짐
    h = h + a # 낮에 올라감
    day = day + 1 # 경과일수 + 1
    
print(day) 
'''

import math

# a: 낮에 올라가는 높이, b: 밤에 미끄러지는 높이, v: 목표 높이
a, b, v = map(int, input().split(' '))

# 달팽이가 올라가야 하는 거리 (v - b)를 달팽이가 매일 올라가는 높이 (a - b)로 나눠준다
# 달팽이가 정상에 도달하는 경우 미끄러지지 않으므로
day = (v -b) / (a - b)

# day는 날짜이므로 소수점이 존재할 수 없어 math.ceil() 함수로 올림
print(math.ceil(day))