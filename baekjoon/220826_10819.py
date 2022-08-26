# 10819 차이를 최대로

from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

max_diff = 0
for i in range(N - 1):
    max_diff = max_diff + abs(nums[i] - nums[i + 1])

perms = list(permutations(nums, N))

for perm in perms:
    diff = 0
    for i in range(N - 1):
        diff = diff + abs(perm[i] - perm[i + 1])
    if diff > max_diff:
        max_diff = diff
        
print(max_diff)