# 1065 한수
n = int(input()) 

# 두자리수 이하는 모두 한수
if n <= 99:
    print(n) # 주어진 수 n을 그대로 출력
    
# 세자리수인 경우
else:
    result = 99 # 99까지 한수
    
    for i in range(100, n + 1): # 100 이상부터 n까지의 한수여부 판별
        
        # 문자열로 변경해 인덱스로 접근 후 정수로 변환
        # 각 자리수의 차이가 일치하는지 확인
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            result = result + 1 # 맞다면 한수 개수 +1
    
    print(result) # 결과 출력