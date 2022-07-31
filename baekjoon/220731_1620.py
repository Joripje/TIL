# 1620 나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split(' '))

pokemons = [input() for i in range(n)]
questions = [input() for i in range(m)]

pokedex = {} # 포켓몬 도감

for idx, pokemon in enumerate(pokemons):
    pokedex[pokemon] = idx + 1
    pokedex[str(idx + 1)] = pokemon # 포켓몬의 이름을 도감번호로, 도감번호를 이름으로 바꾸기 위한 도감 생성
    
for question in questions:
    print(pokedex.get(question))