# 1929 소수 구하기

# 에라토스테네스의 체를 이용해 풀이
# N까지의 소수 리스트를 만들고 범위에 맞춰 출력

M, N = map(int, input().split())

# 에라토스테네스의 체
numbers = [1] * (N + 1) # N까지 인덱스를 가지는 1차원 배열 생성
numbers[0] = 0
numbers[1] = 0 # 1은 소수 아님

for i in range(1, N + 1): # 배열을 순회
    if numbers[i] == 1: # 지워지지 않은 첫번째 수를 만나면
        for j in range(2, N // i + 1): # 해당 수를 제외한 배수 전부 제거
            numbers[i * j] = 0
            
# 값이 1이면 해당 인덱스는 소수
# enumerate로 해당 값을 가져오고 범위에 맞춰 출력
for idx, number in enumerate(numbers):
    if number and idx >= M:
        print(idx)