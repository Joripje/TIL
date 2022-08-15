# 10844 쉬운 계단 수

## 딕셔너리를 사용하여 풀이
## 각 숫자의 개수를 세는 딕셔너리를 만듦
## 0과 9는 1과 8이 다음에 온다
## 나머지는 -1 +1 값이 온다

stair = {0 : 0, 1 : 1, 2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 1, 7 : 1, 8 : 1, 9 : 1}

N = int(input())

for i in range(N - 1):
    n_stair = {x: 0 for x in range(10)}
    for j in range(10):
        if j == 0:
            n_stair[1] = n_stair[1] + stair[j]
        elif j == 9:
            n_stair[8] = n_stair[8] + stair[j]
        else:
            n_stair[j - 1] = n_stair[j - 1] + stair[j]
            n_stair[j + 1] = n_stair[j + 1] + stair[j]
    stair = n_stair
    
    
print(sum(stair.values()) % 1000000000)