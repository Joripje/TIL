"""1802 종이 접기
종이를 반씩 접어서 확인
접어서 겹치는 부분의 방향이 서로 달라야 한다
"""

T = int(input())  # 테스트 케이스 개수

for _ in range(T):  # 테스트 케이스만큼 반복
    paper = input()  # 종이의 정보
    N = len(paper)  # 종이의 길이
    flag = 1  # 종이가 규칙대로 접히면 1, 아니면 0이 되는 flag
    while N != 1:  # 종이의 길이가 1이 되면 종료한다

        for i in range(N // 2):
            if paper[i] == paper[N - i - 1]:  # 종이를 반 접어서 겹치는 부분의 방향이 같다면
                flag = 0  # 규칙대로 접히지 않으므로 flag 0
                break  # 더 이상 확인하지 않아도 된

        if flag:  # 반 접었을 때 겹치는 부분이 전부 달랐다면
            N //= 2  # 한 번 더 반을 접어서 확인
        else:
            break

    if flag:  # 규칙에 맞다면 flag는 1
        print('YES')

    else:  # 규칙에 맞지 않다면 flag는 0
        print('NO')