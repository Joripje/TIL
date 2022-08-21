# 3085 사탕 게임

N = int(input())

candies = [[0] * (N + 2)]
for i in range(N):
    candies.append([0] + list(input()) + [0])
candies.append([0] * (N + 2))

max_candies = 0

# 가로 탐색
for i in range(1, N + 1):
    for j in range(1, N):
        if candies[i][j] != candies[i][j + 1]:
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
            
            for k in range(1, N + 1):
                candy = 1
                for l in range(1, N + 2):
                    if candies[k][l] != candies[k][l - 1]:
                        if candy > max_candies:
                            max_candies = candy
                        candy = 1
                    elif candies[k][l] == candies[k][l - 1]:
                        candy = candy + 1
            
            for k in range(1, N + 1):
                candy = 1
                for l in range(1, N + 2):
                    if candies[l][k] != candies[l - 1][k]:
                        if candy > max_candies:
                            max_candies = candy
                        candy = 1
                    elif candies[l][k] == candies[l - 1][k]:
                        candy = candy + 1
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]

# 세로 탐색
for i in range(1, N + 1):
    for j in range(1, N):
        if candies[j][i] != candies[j + 1][i]:
            candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
            
            for k in range(1, N + 1):
                candy = 1
                for l in range(1, N + 2):
                    if candies[k][l] != candies[k][l - 1]:
                        if candy > max_candies:
                            max_candies = candy
                        candy = 1
                    elif candies[k][l] == candies[k][l - 1]:
                        candy = candy + 1
            
            for k in range(1, N + 1):
                candy = 1
                for l in range(1, N + 2):
                    if candies[l][k] != candies[l - 1][k]:
                        if candy > max_candies:
                            max_candies = candy
                        candy = 1
                    elif candies[l][k] == candies[l - 1][k]:
                        candy = candy + 1
            candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]

print(max_candies)