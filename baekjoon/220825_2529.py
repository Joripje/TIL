# 2529 부등호

from itertools import permutations
N = int(input())
inequals = list(input().split())
nums = list(range(10))
perms = list(permutations(nums, N + 1))
results = []

for perm in perms:
    correct = 1
    for i in range(N):
        if inequals[i] == '>':
            if not perm[i] > perm[i + 1]:
                correct = 0
                break
        elif inequals[i] == '<':
            if not perm[i] < perm[i + 1]:
                correct = 0
                break
    if correct:
        a = ''
        for j in range(N + 1):
            a = a + str(perm[j])
        results.append(int(a))
        
max_sum = max(results)
min_sum = min(results)

if len(str(max_sum)) == N:
    max_sum = '0' + str(max_sum)

if len(str(min_sum)) == N:
    min_sum = '0' + str(min_sum)

print(max_sum)
print(min_sum)