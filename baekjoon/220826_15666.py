# 15666 N과 M (12)

from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = set()

perms = list(combinations_with_replacement(nums, M))

if M != 1:
    for perm in perms:
        result.add(tuple(sorted((perm))))

else:
    result = set(perms)
    
result = sorted(result)

for sets in result:
    print(*sets, sep=' ')