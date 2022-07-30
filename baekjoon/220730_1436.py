# 1436 영화감독 숌

# 무한반복으로 목표에 도달할때까지 탐색
# 1부터 차례로 확인해봄

n = int(input())


final_num = 666 # 666이 첫 번째 종말의 수이므로 666부터 시작
final_count = 0 # n번째 종말의 수인지 세기 위해 변수 설정

while final_count < n: # n번째 종말의 수에 도달할때까지
    if str(final_num).find('666') != -1: 
        final_count = final_count + 1 # 666이 들어가는 숫자라면 카운트 증가
    final_num = final_num + 1 # 다음 숫자로 넘어가며 탐색
        
print(final_num - 1) # 결과 출력