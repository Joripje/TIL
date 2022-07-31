# 10816 숫자 카드 2

n = int(input())
cards = list(map(int, input().split(' ')))

cards_dict = {} # 카드의 개수를 셀 딕셔너리 생성 (카드 숫자 : 개수(int) 형태) 

for card in cards:
    if cards_dict.get(card): 
        cards_dict[card] = cards_dict[card] + 1 # 이미 기록한 카드라면 개수 + 1
    else:
        cards_dict[card] = 1 # 새롭게 추가되는 카드라면 값에 1 할당
    
m = int(input())
nums = list(map(int, input().split(' ')))

for num in nums:
    print(cards_dict.get(num, 0), end = ' ') # 해당 숫자 카드가 존재하면 개수 출력, 없다면 0 출력