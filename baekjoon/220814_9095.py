# 9095 1, 2, 3 더하기

# 동적 계획법
# 거스름돈 경우의 수와 같음
# 3 , n - 3 경우의 수
# 2 , n - 2 경우의 수
# 1 , n - 1 경우의 수 모두 더함

T = int(input())

for tc in range(T):
    n = int(input())
    
    sums = [1, 1] + [0] * (n - 1)  # 각 숫자별 1, 2, 3 합 조합, 1은 1가지
    
    if n >= 2:  # 2 이상인 경우 2에 2가지 넣고 시작
        sums[2] = 2
    
    # 순회하며 목표 정수까지 경우의 수 탐색
    for i in range(3, n + 1):
        sums[i] = sums[i] + sums[i - 1]  # 1 + (n - 1 숫자 조합)의 경우의 수
        sums[i] = sums[i] + sums[i - 2]  # 2 + (n - 2 숫자 조합)의 경우의 수
        sums[i] = sums[i] + sums[i - 3]  # 3 + (n - 3 숫자 조합)의 경우의 수
        
    print(sums[n])  # 결과 출력