# 16194 카드 구매하기 2

# 1부터 N으로 N 만들기
# N을 만들때 숫자x가격
# 이때 N을 만드는 모든 경우에서 최소값으로

N = int(input())
P = list(map(int, input().split()))

price = {p: P[p - 1] for p in range(1, N + 1)}  # 카드팩의 가격을 저장한 딕셔너리

cards = [0] * (N + 1)  # 카드의 최소 가격을 저장할 배열

for i in range(1, N + 1):
    prices = []  # i장의 카드를 만드는 방법들의 가격 리스트
    for j in range(1, i + 1):
        prices.append(price[j] + cards[i - j])  # i장의 카드를 만드는 방법의 카드 가격 추가
    cards[i] = min(prices)  # 여러 방법 중 가장 가격이 낮은 경우를 저장
    
print(cards[N])