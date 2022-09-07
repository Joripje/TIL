# 16198 에너지 모으기

from itertools import permutations

N = int(input())
energy = list(map(int, input().split()))

perms = list(permutations(list(range(1, N - 1)), N - 2))

max_energy = 0

for perm in perms:
    empty = [0] * N
    energi = 0
    for i in perm:
        empty[i] = 1
        l = i -1
        r = i + 1
        while empty[l]:
            l = l - 1
        while empty[r]:
            r = r + 1
        energi = energi + energy[l] * energy[r]
    if max_energy < energi:
        max_energy = energi
        
print(max_energy)