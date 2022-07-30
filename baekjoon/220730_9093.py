# 9093 단어 뒤집기

n = int(input())
sentences = [input().split(' ') for i in range(n)] # 각 문장을 입력받아 리스트에 저장

for sentence in sentences: # 문장 리스트를 순회
    for word in sentence: # 문장의 각 단어를 순회
        # 출력 기준을 맞추기 위한 조건문
        if word != sentence[-1]:
            print(word[::-1], end = ' ')  # 마지막 단어가 아니면 뒤집어진 단어를 출력하고 띄어쓰기
        else:
            print(word[::-1]) # 마지막 단어라면 뒤집어진 단어를 출력하고 줄바꿈