# 2941 크로아티아 알파벳
word = input()

# 크로아티아 알파벳 리스트
c_alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 


for alpha in c_alphas:              # 크로아티아 알파벳 리스트 순회
    word = word.replace(alpha, '1') # .replace() 메서드 사용
                                    # 변경된 크로아티아 알파벳을 임의의 문자로 변경

print(len(word)) # 알파벳 개수 출력