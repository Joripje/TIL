# 1564 팩토리얼5
# 연산속도를 줄이기 위해 뒷자리만 사용하여 정답 조건에 맞는 답을 구함
# 자리수가 달라지면 결과도 달라짐
# 수학적 지식 필요

n = int(input())

result = 1

# 반복문으로 1부터 n까지 정수를 곱함
for i in range(1, n + 1):
    result = result * i
    
    while str(result)[-1] == '0': # 뒷자리 0은 필요 없으므로 제거
        result = int(str(result)[:-1])
    

    result = int(str(result)[-12:]) # 마지막 숫자만 사용하며 계산을 이어감
                                   # 자리수에 따라 결과가 다름???
    
print(('00000' + str(result))[-5:]) # 5자리 형식을 맞추기 위해 문자열 0 추가