# 11726 2xn 타일링

# 동적 계획법
# 1차원 배열에 각 값의 수를 저장
# n번째 항은 n - 1, n - 2 항의 합과 같다(?)

n = int(input())

tile = [1, 1] + [0] * (n - 1)  # n항까지 값을 저장할 1차원 배열, 2x1은 1가지


for i in range(2, n + 1):
    tile[i] = tile[i - 1] + tile[i - 2]
    
print(tile[n] % 10007)