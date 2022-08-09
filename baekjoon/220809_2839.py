# 2839 설탕배달
# 완전검색을 사용하지 않고 풀이

n = int(input())

result = 0  # 설탕봉지 수

while n > 0:  # 남은 설탕이 0 이하라면 종료
    if n % 5 == 0:  # 5로 나누어 떨어진다면
        result = result + (n // 5)  # 5로 나눈 몫을 결과에 추가
        n = 0
        break  # 반복문 종료
    else:  # 나누어 떨어지지 않는다면
        n = n - 3  # 3킬로 봉지 하나 추가
        result = result + 1

# 나누어 떨어지면 n = 0, 결과값 출력, 아니라면 나누어 떨어지지 않음 -1 출력
if n:
    print(-1)
else:
    print(result)