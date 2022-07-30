# 1920 수 찾기

# 입력값 저장
n = int(input())
A = list(map(int, input().split(' '))) 
m = int(input())
m_l = list(map(int, input().split(' ')))

# 딕셔너리를 사용해 주어진 수들이 A에 존재하는지 확인
A_dict = {} 

for n in A: # 정수 리스트 A를 순회하며
    A_dict[n] = 1 # 정수를 key로 가지는 딕셔너리 만들기
    
# .get() 메서드를 사용해 A에 존재하는 값인지 확인
# 해당 key 존재하면 값인 1을 출력, key가 없으면 0을 반환해 출력
for i in m_l:
    print(A_dict.get(i, 0))