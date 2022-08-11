# 4948 베르트랑 공준

# 조건에 맞는 소수 리스트 만들기
prime = [0] + [1] * (123456 * 2)
prime[1] = 0
for i in range(1, int(len(prime) ** 0.5) + 1):
    if prime[i] == 1:
        for j in range(2, len(prime) // i + 1):
            prime[j * i] = 0
            
while True:
    n = int(input())
    if n:
        count = 0
        for i in range(n + 1, 2 * n + 1):
            if prime[i]:
                count = count + 1
        print(count)
    
    else:
        break