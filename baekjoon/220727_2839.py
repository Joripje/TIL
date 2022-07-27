# 2839 설탕 배달
N = int(input())

n = N // 5 # 설탕 조합에서 가질 수 있는 5kg 설탕 최대 개수

m = N // 3 # 설탕 조합에서 가질 수 있는 3kg 설탕 최대 개수

sum_list = [] # 설탕 봉지 총 개수 리스트

# 정확히 Nkg이 되는 설탕 조합 봉지 개수 구하기
for i in range(n + 1):
    for j in range(m + 1):
        if (5 * i) + (3 * j) == N: # 정확히 Nkg이 되는 조합일 경우
            sum_list.append(i + j) # 5kg과 3kg 봉지 개수의 합을 리스트에 추가
            
if sum_list:
    print(min(sum_list)) # 조합의 최소 개수 출력

else:
    print(-1) # 조합이 존재하지 않으면 -1 출력