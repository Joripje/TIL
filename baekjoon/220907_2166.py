# 2166 다각형의 면적
# 변의 길이가 다른 다각형 넓이 구하기
# 위키하우 다각형 넓이 공식 구현
N = int(input())
dot = [tuple(map(int, input().split()))]
dots = [tuple(map(int, input().split())) for _ in range(N - 1)]
dots = dot + dots + dot

A = 0
B = 0

for i in range(N):
    A = A + dots[i][0] * dots[i + 1][1]
    
for j in range(N):
    B = B + dots[j][1] * dots[j + 1][0]
    
s = round(abs((A - B) / 2), 1)

print(s)