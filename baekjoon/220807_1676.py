# 1676 팩토리얼 0의 개수

n = int(input())

result = 1
count = 0

if n > 1:
    for i in range(2, n + 1):
        result = result * i

while str(result)[-1] == '0':
    result = int(str(result)[:-1])
    count = count + 1
    
print(count)