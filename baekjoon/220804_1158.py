# 1158 요세푸스 문제

# 회전초밥이 무한이 돌고 있음
# 항상 k번째 초밥을 집음
# 집은 초밥을 기록해 출력
# 레일이 비면 끝

n, k = map(int, input().split(' '))

sarams = list(range(1, n + 1)) # 회전초밥의 리스트
eli_saram = [] # 집은 초밥을 기록
count = 0 # k번째에 집기 행동을 하기 위한 카운트

result = []

while sarams:
    for i in range(len(sarams)): # 회전초밥 돌아감
        if count % k == k - 1: # k번째 초밥 집기
            eli_saram.append(sarams[i])
            result.append(sarams[i])
        count = count + 1 # 행동 카운트 증가

    if eli_saram: # 집은 초밥이 있으면 초밥 없애기
        for saram in eli_saram:
            sarams.remove(saram)
        eli_saram = []

# 결과 출력
print('<', end ='')
for i in result[:-1]:
    print(i, end = ', ')
print(f'{result[-1]}>')