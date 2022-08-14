# 2193 이친수

N = int(input())

pin = [0] * (N + 1)
pin[1] = 1

for i in range(2, N + 1):
    pin[i] = pin[i - 1] + pin[i - 2]
    
print(pin[N])