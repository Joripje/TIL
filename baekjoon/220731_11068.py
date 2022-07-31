# 11068 회문인 수

# 10진법 함수를 n진법으로 변환할 함수 작성
def njinbub(num, n): 
    char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-' # 64진법까지 나타낼 수 있는 64개의 문자표
    
    # n으로 나눈 몫이 다음 함수의 인자로 들어가야 한다
    if num // n == 0: # n으로 나눈 몫이 0일 경우 함수 종료
        return char[num % n] # 나머지값을 문자표에서 찾아 반환
    
    else:
        return njinbub(num // n, n) + char[num % n] # 그 외의 경우 n으로 나눈 몫으로 함수 호출

n = int(input())
nums = [int(input()) for i in range(n)]

# 주어진 숫자 리스트를 순회하며 함수를 사용해 회문판별
for num in nums:
    result = 0 # 회문 결과값(회문이 아니라면 0, 회문이면 1)
    
    for i in range(2, 65): #  B진법 (2 ≤ B ≤ 64)으로 표현한 수 회문 판별
        check_num = njinbub(num, i)
        
        if check_num == check_num[::-1]: # B진법이 회문이라면 결과를 1로 변경하고 해당 숫자 판별 종료
            result = 1
            break
            
    print(result)