# 9020 골드바흐의 추측

# 소수 리스트를 생성(최대 정수값까지)
# 주어진 숫자 범위 내의 리스트를 순회하며 두 수의 합이 n이 되는 두 수를 뽑아냄
# 두 소수의 차가 가장 작은 것을 출력

# 최대 정수까지 소수 리스트 생성(에라토스테네스의 체)

numbers = [0] * 2 + [1] * 9999 # 소수 판별을 위한 1차원 배열 생성, 값이 1인 인덱스는 소수

for i in range(2, int(10000 ** 0.5) + 1):
    if numbers[i]: # 지워지지 않은 수를 만나면
        for j in range(2, 10000 // i + 1): # 해당 수의 배수 전부 지우기
            numbers[i * j] = 0
        

# 테스트 케이스 입력
T = int(input())
for tc in range(T):
    n = int(input())
        
    # 1차원 배열을 순회하며 소수인 두 값을 더해 주어진 수가 되는지 확인
    for i in range(n // 2 , n + 1): # 중앙부터 찾으면 두 소수의 차이가 가장 작음
        if numbers[i] and numbers[n - i]: # i가 소수일때 n - 1인 소수가 있다면 조합이 존재
            print(n - i, i)
            break