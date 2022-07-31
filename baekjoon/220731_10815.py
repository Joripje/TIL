# 10815 숫자 카드

n = int(input())
cards = list(map(int, input().split(' ')))

cards_dict = {}

for card in cards:
    cards_dict[card] = 1 # 카드의 숫자가 중복되지 않으므로 딕셔너리 키로 사용
    
m = int(input())
nums = list(map(int, input().split(' ')))

for num in nums:
    print(cards_dict.get(num, 0), end = ' ') # 해당 숫자 카드가 존재하면 값 1 출력, 없다면 0 출력