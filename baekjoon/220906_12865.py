# 12865 평범한 배낭
'''
동적계획법을 이용해 풀이
배낭의 최대 무게까지 각 무게 조합의 최대 가치를 리스트에 저장
배낭에 같은 물건을 넣을 수 없다
물건 기록을 set으로 만들어 `in` 연산을 빠르게
'''
N , K = map(int, input().split())

back_pack = [[0, set()] for _ in range(K + 1)]  # 가치 합과 들어있는 물건이 기록된 배낭
items = [tuple(map(int, input().split())) for _ in range(N)]  # (무게, 가치) 리스트
max_value = 0  # 가치 최댓값을 저장할 변수

# 배낭에 채울 수 있는 용량 내에서 가치의 합의 최대값을 구함
for i in range(1, K + 1):
    max_val = 0
    
    for idx, item in enumerate(items):  # 물건들을 순회하며 가치합을 구함
        if item[0] <= i and not idx in back_pack[i-item[0]][1]:  # 물건이 배낭 용량보다 작고 배낭에 담지 않은 물건이라면
            val = item[1] + back_pack[i-item[0]][0]  # 해당 물건의 가치와 (무게 = 용량 - 물건의 무게)일 때 최대 가치를 더한다
            
            if val >= max_val:  # 해당 가치의 합이 현재 무게에서 최대값이라면
                max_val = val  # 값을 기록
                back_pack[i][0] = val
                back_pack[i][1] = back_pack[i-item[0]][1] | {idx}  # 배낭에 들어있는 물건 기록

    if max_val > max_value:  # 구한 값이 현재 최대값보다 크다면 값을 저장
        max_value = max_val
        
print(max_value)  # 최대값 출력