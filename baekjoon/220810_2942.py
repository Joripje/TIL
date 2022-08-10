# 2942 퍼거슨과 사과

## 공약수로 두 수를 나눈 값을 출력하는 문제
## 최대 공약수의 약수는 공약수
## 최대 공약수로 공약수를 구해 각 값을 나누어 준다

R, G = map(int, input().split())

# 최대 공약수를 구하는 함수
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
rg_gcd = gcd(R, G)

cd_list = [] # 공약수를 넣어줄 리스트

# 최대 공약수의 약수 구하기
for i in range(1, int(rg_gcd ** 0.5) + 1): # 제곱근의 값까지만
    
    if rg_gcd % i == 0: # i가 rg_gcd의 약수라면, rg_gcd를 i로 나눈 값도 rg_gcd의 약수가 된다
        cd_list.append(i)
        
        if rg_gcd // i != i: # 같은 값이 추가되면 안됨
            cd_list.append(rg_gcd // i)
            
for cd in cd_list:
    print(f'{cd} {R // cd} {G //cd}')