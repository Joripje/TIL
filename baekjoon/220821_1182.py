# 1182 부분수열의 합

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for i in range(1, 1 << N):
    subset_sum = 0
    for j in range(N):
        if i & (1 << j):
            subset_sum = subset_sum + numbers[j]
    if subset_sum == S:
        result = result + 1
        
print(result)