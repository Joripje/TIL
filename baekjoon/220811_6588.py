# 6588 골드바흐의 추측

# 소수 리스트를 생성(최대 정수값까지)
# 주어진 숫자 범위 내의 리스트를 순회하며 두 수의 합이 n이 되는 두 수를 뽑아냄
# b-a가 가장 큰 것, 첫번째 구해지는 조합이 가장 크다
# 없으면 Goldbach's conjecture is wrong. 출력

# 최대 정수까지 소수 리스트 생성(에라토스테네스의 체)

numbers = [0] * 2 + [1] * 999999 # 소수 판별을 위한 1차원 배열 생성, 값이 1인 인덱스는 소수

for i in range(2, int(1000000 ** 0.5) + 1):
    if numbers[i]: # 지워지지 않은 수를 만나면
        for j in range(2, 1000000 // i + 1): # 해당 수의 배수 전부 지우기
            numbers[i * j] = 0
            
# 문제에서 2는 사용하지 않음
numbers[2] = 0

# 테스트 케이스 입력

while True:
    n = int(input())
    if n == 0:
        break

    else:
        fail = True
        
        # 1차원 배열을 순회하며 소수인 두 값을 더해 주어진 수가 되는지 확인
        for i in range(int(n // 2) + 2):
            if numbers[i] and numbers[n - i]: # i가 소수일때 n - 1인 소수가 있다면 조합이 존재
                    print(f'{n} = {i} + {n - i}') # 첫번째 나오는 조합이 b - a가 최대이므로 출력하고 반복 종료
                    fail = False
                    break
                    
        # 출력하지 못했다면 해당 문구 출력
        if fail:
            print("Goldbach's conjecture is wrong.")